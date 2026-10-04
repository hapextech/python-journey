# Anagram Finder 
# Suggested time: 15–20 minutes
# Problem
# Check if two words are anagrams of each other (meaning they contain the exact same characters in the exact same frequencies, just in a different order). 
# Examples
# Input: Word 1: listen | Word 2: silent → Output: Anagram
# Input: Word 1: triangle | Word 2: integral → Output: Anagram
# Input: Word 1: apple | Word 2: pale → Output: Not an anagram
# Input: Word 1: hello | Word 2: billion → Output: Not an anagram 
# Constraints
# Do not use sorted() or collections.Counter.
# You must build a character frequency map manually (using a dictionary) to compare the letters.
# Treat uppercase and lowercase as the same (e.g., Triangle and integral should match).
# Do not import external libraries. 

def anagram(word1, word2):
    word1 = word1.lower().strip()
    word2 = word2.lower().strip()

    if len(word1) != len(word2):
        return "Nor an Anagram"

    dic1 = {}
    
    for char in word1:
        if char in dic1:
            dic1[char] += 1
        else:
            dic1[char] = 1

    dic2 = {}      
    for cha in word2:
        if cha in dic2:
            dic2[cha] += 1
        else:
            dic2[cha] = 1
    if dic1 == dic2:
        return "Anagram"
    else:
        return "Not Anagram"

print(anagram("apple","pale"))
    