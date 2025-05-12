# Group Anagrams Together

from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams["".join(sorted(word))].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    words = ["bat", "tab", "cat", "act"]
    print(f"Grouped Anagrams: {group_anagrams(words)}")