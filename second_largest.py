# Second Largest

# Problem
# Given a list of numbers, find the second-largest unique number.
# Examples
# Input: [10, 5, 8, 20, 15]  →  Output: 15
# Input: [4, 9, 2, 9, 7]    →  Output: 7
# Constraints
# You are strictly forbidden from using sort(), sorted(), max(), or converting the list to a set().
# You must track the largest and second_largest variables manually and update them in a single pass (one loop) through the list.
# Duplicate values must not affect the result.

Input = [10, 5, 8, 20, 15]

largest_number = 0
second_largest = 0

for x in Input:
    if x > largest_number:
        second_largest = largest_number
        largest_number = x
    else:
        if x > second_largest:
            second_largest = x
print(second_largest)

