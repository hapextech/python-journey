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
    user_input = "".join(x for x in user_input if x.isalnum())
    user_input = user_input.lower()
    # print(user_input)
    left_pointer = 0
    right_pointer = len(user_input) - 1

    while left_pointer < right_pointer:
        if user_input[left_pointer] != user_input[right_pointer]:
            return "input not a palindrome"
        else:
            # ispalindrome = True
            left_pointer += 1
            right_pointer -= 1
        return "input is a palindrome"
        
            
        
print(palindrome("Hello, World!"))
