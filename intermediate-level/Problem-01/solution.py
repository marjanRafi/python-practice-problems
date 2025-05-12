# Longest Word in a Sentence

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

if __name__ == "__main__":
    input_sentence = "Machine learning is fascinating"
    print(f"Longest Word: {longest_word(input_sentence)}")