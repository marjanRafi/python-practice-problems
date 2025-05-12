# Factorial Using Recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    number = 5
    print(f"Factorial of {number}: {factorial(number)}")