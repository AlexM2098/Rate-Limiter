import time

class TokenBucket:
    def __init__(self, rate=5, capacity=5):
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill_time = time.time()

    def consume(self):
        now = time.time()
        time_since_last_refill = now - self.last_refill_time
        refill_amount = time_since_last_refill * self.rate
        self.tokens = min(self.tokens + refill_amount, self.capacity)
        self.last_refill_time = now

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

    def next_refill_time(self):
        return self.last_refill_time + (1 / self.rate)
