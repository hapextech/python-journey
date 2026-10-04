# Two Sum
# Suggested time: 20–25 minutes
# Problem
# Given a list of numbers and a target number, find the first valid pair of numbers whose sum equals the target. Return their indices (positions). 
# Examples
# Numbers: [2, 7, 11, 15] | Target: 9 → Output: [0, 1] 
# Constraints
# You must return the indices of the two numbers, not the numbers themselves.
# You must achieve O(n) time complexity by using a dictionary to track the numbers you've seen so far.
# Nested loops (O(n²)) are strictly forbidden.
# The two numbers must come from different positions in the list. 


def two_sum(Numbers, target):
    seen = {}
    
    for i, num in enumerate(Numbers):
        res = target - num 
        if res in seen:
            return seen[res], i
        else: 
            seen[num] = i

    

print(two_sum([2, 7, 11, 15], 9))


