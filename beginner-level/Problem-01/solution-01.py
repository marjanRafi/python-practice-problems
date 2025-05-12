# Reverse a String Without Slicing
 
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

if __name__ == "__main__":
    input_str = "bongodev"
    print(f"Original: {input_str}")
    print(f"Reversed: {reverse_string(input_str)}")