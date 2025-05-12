# Check if a Word is a Palindrome

def is_palindrome(word):
    word = ''.join(filter(str.isalnum, word)).lower()
    return word == word[::-1]

if __name__ == "__main__":
    word = "Madam"
    print(f"Is Palindrome: {is_palindrome(word)}")