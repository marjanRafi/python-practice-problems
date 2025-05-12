# Sum of Digits of an Integer

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

if __name__ == "__main__":
    number = 9875
    print(f"Sum of Digits: {sum_of_digits(number)}")