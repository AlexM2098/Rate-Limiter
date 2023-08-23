import logging
from django.http import JsonResponse
import time
from myapp.token_bucket import TokenBucket


logger = logging.getLogger(__name__)

class RateLimiterMiddleware:
    def __init__(self, get_response, rate=5, capacity=5):
        self.get_response = get_response
        self.rate = rate
        self.capacity = capacity
        self.token_buckets = {}

    def __call__(self, request):
        user_id = self.get_user_id(request)
        token_bucket = self.token_buckets.get(user_id)

        if not token_bucket:
            token_bucket = TokenBucket(rate=self.rate, capacity=self.capacity)
            self.token_buckets[user_id] = token_bucket

        if not token_bucket.consume():
            logger.warning(f"Rate limit exceeded for user: {user_id}")
            response_data = {"message": "Rate limit exceeded"}
            response = JsonResponse(response_data, status=429)
            
            # Add rate limit headers
            response['X-RateLimit-Limit'] = self.capacity
            response['X-RateLimit-Remaining'] = 0
            response['X-RateLimit-Reset'] = int(token_bucket.next_refill_time())
            return response

        response = self.get_response(request)
        
        # Add rate limit headers
        response['X-RateLimit-Limit'] = self.capacity
        response['X-RateLimit-Remaining'] = token_bucket.tokens
        response['X-RateLimit-Reset'] = int(token_bucket.next_refill_time())

        return response

    def get_user_id(self, request):
        return request.META['REMOTE_ADDR']  # Use IP address as user identifier

