# Find Duplicates in a List

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

if __name__ == "__main__":
    tags = ["ai", "ml", "python", "ml", "dl", "ai"]
    print(f"Duplicates: {find_duplicates(tags)}")