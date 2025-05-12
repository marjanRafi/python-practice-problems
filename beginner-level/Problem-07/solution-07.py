# Find Missing Number in a Sequence

def find_missing_number(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

if __name__ == "__main__":
    sequence = [1, 2, 4, 5]
    print(f"Missing Number: {find_missing_number(sequence)}")