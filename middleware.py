from django.http import JsonResponse
import time

class RateLimiterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate = 5 / 60  # 5 requests per minute
        self.capacity = 5
        self.token_buckets = {}  # Dictionary to store TokenBucket instances for each user (or IP)

    def __call__(self, request):
        user_id = self.get_user_id(request)  # Replace this with your method to get the user's ID or IP address
        
        # Initialize a new TokenBucket if it doesn't exist for this user
        if user_id not in self.token_buckets:
            self.token_buckets[user_id] = TokenBucket(rate=self.rate, capacity=self.capacity)
        
        token_bucket = self.token_buckets[user_id]
        
        # Check if the request should be allowed
        if token_bucket.consume():
            response = self.get_response(request)
        else:
            response_data = {"message": "Rate limit exceeded"}
            response = JsonResponse(response_data, status=429)

        return response
    
    def get_user_id(self, request):
        # Implement your logic here to get the user's ID or IP address
        # For simplicity, we'll use a placeholder here
        return "some_user_id"

class TokenBucket:
    def __init__(self, rate, capacity):
        """
        Initialize a token bucket.
        
        Parameters:
        - rate: The rate at which tokens are added per second
        - capacity: The maximum number of tokens the bucket can hold
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity  # Initially, the bucket is full
        self.last_refill_time = time.time()  # Record the last time the bucket was refilled
        
    def refill(self):
        """
        Refill tokens in the bucket based on the time elapsed.
        """
        current_time = time.time()
        time_elapsed = current_time - self.last_refill_time
        
        # Calculate the number of tokens to add based on the time elapsed and rate
        tokens_to_add = time_elapsed * self.rate
        self.tokens = min(self.tokens + tokens_to_add, self.capacity)
        
        # Update the last refill time
        self.last_refill_time = current_time
    
    def consume(self):
        """
        Consume a token if available and return True, otherwise return False.
        """
        # First, refill the tokens
        self.refill()
        
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

# Testing the TokenBucket class
test_bucket = TokenBucket(rate=5/60, capacity=5)
test_bucket.tokens  # Should show the initial tokens as 5

