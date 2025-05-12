# Most Frequent Word (Excluding Stopwords)

from collections import Counter
import string

def most_frequent_word(text, stopwords):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [word for word in words if word not in stopwords]
    return Counter(words).most_common(1)[0][0]

if __name__ == "__main__":
    text = "This is a test. This is another test."
    stopwords = {"this", "is", "a", "the"}
    print(f"Most Frequent Word: {most_frequent_word(text, stopwords)}")