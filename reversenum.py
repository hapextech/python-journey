# Number Reverser 
# Suggested time: 15–20 minutes
# Problem
# Reverse a given integer. For example, 12345 becomes 54321. 
# Examples
# Input: 12345 → Output: 54321
# Input: -987 → Output: -789
# Input: 1200 → Output: 21 (Mathematically, leading zeros are dropped)
# Input: 0 → Output: 0 
# Constraints
# You are NOT allowed to convert the integer to a string (no str(), no string slicing like [::-1]).
# You must use pure mathematical operations (specifically modulo % to get the last digit, and integer division // to remove the last digit).
# Must handle negative numbers correctly (the negative sign should remain at the front).
# Do not import libraries. 

def reverse_num(num):
    isnegative = False
    if num < 0:
        isnegative = True
        num = num * -1
    res = 0
    while num > 0:
        rev = num % 10
        res = res * 10 + rev
        num = num // 10
    
    if isnegative:
        res = res * -1
    
    return res
print(reverse_num(-54321))
