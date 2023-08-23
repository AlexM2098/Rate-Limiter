# My Django Project with Rate Limiting

## Rate Limiter
This project implements a rate limiter using the token bucket algorithm.

### Rate Limit Rules
- 5 requests per minute per user/IP.

### Behavior
- When the rate limit is exceeded, the user will receive a JSON response: `{"message": "Rate limit exceeded"}` with HTTP status 429.

## Testing the Rate Limiter
Navigate to `/test/` and try making more than 5 requests within a minute.
