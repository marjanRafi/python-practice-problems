# Count Vowels in a Sentence

def count_vowels(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence.lower():
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    sentence = "Data Science is awesome"
    print(f"Vowel Count: {count_vowels(sentence)}")