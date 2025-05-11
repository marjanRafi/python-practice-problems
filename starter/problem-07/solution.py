def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return "Not a Fizz-buzz number"

# Example usage
number = 15
result = fizz_buzz(number)
print(f"The result for {number} is: {result}")

number = 9
result = fizz_buzz(number)
print(f"The result for {number} is: {result}")

number = 10
result = fizz_buzz(number)
print(f"The result for {number} is: {result}")

number = 7
result = fizz_buzz(number)
print(f"The result for {number} is: {result}")
