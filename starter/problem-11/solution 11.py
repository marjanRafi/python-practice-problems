from collections import Counter

rhyme = 'Twinkle, twinkle, little star. How I wonder what you are!'

def most_frequent_char(paragraph):
 
    cleaned_paragraph = ''.join(e for e in paragraph if e.isalnum())
    
    char_count = Counter(cleaned_paragraph.lower())
    
    most_common_char, frequency = char_count.most_common(1)[0]
    
    return most_common_char, frequency

char, freq = most_frequent_char(rhyme)
print(f"The most frequent character is '{char}' with {freq} occurrences.")
