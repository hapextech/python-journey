# 2. Palindrome
# Suggested time: 20–25 minutes
# Problem
# Write a program that determines whether a full sentence reads the same forwards and backwards, ignoring mixed casing, spaces, and punctuation (e.g., "Was it a car or a cat I saw?" is a palindrome). 
# Examples
# Input: Was it a car or a cat I saw? → Output: Palindrome
# Input: Hello, World! → Output: Not a palindrome 
# Constraints
#  Must be implemented using a strict two-pointer approach (left and right indices moving inward).
# 7. You are not allowed to create any new reversed strings, substrings, or use built-in string reversal methods (like [::-1] or .reverse()).
# You must manually skip spaces and punctuation during the pointer comparison.
# Do not import libraries

def palindrome(user_input):
    punctuation = (" ,?!")
    for i, x in enumerate(user_input):
        left_pointer = user_input[-1]
        right_pointer = user_input[0]
