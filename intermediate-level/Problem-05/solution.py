# Fibonacci Using Memoization

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    number = 50
    print(f"Fibonacci of {number}: {fibonacci(number)}")