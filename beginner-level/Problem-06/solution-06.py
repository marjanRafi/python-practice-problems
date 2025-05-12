# Capitalize First Letter of Each Word

def capitalize_words(text):
    return ' '.join(word[0].upper() + word[1:] for word in text.split())

if __name__ == "__main__":
    input_text = "python for web developers"
    print(f"Capitalized: {capitalize_words(input_text)}")