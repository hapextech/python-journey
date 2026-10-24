# Problem
# Given a list and a target value, find every index where the target appears. Print all matching indices, the total count of matches, and the index of the first and last occurrence. If the target does not appear, print a not-found message.
# Examples
# Starting list: values = [14, 7, 22, 9, 7, 31, 7, 5]
# Target: 7 → Found at indices: [1, 4, 6] | Count: 3 | First: 1 | Last: 6
# Target: 22 → Found at indices: [2] | Count: 1 | First: 2 | Last: 2
# Target: 18 → Target not found
# Constraints
# Use a loop; do not use .index(), .count(), or list comprehensions.
# Do not stop at the first match — you must find all occurrences.
# Do not import libraries.
# Do not hardcode the answer.
# What This Tests: Lists, loops, comparisons, indexing, building a results list, and tracking multiple pieces of state in one pass.


def linear_search(input, target):
    if target not in input:
        return f"Target: {target} → Target not found"
   
    found = []

    for index, num in enumerate(input):
        if num == target:
            found.append(index)
        
    print(found)
    count = len(found)
    first = found[0]
    last = found[-1]

    return f"Target: {target} → Found at indices {found} | Count: {count} | First: {first} | Last: {last}"

print(linear_search([14, 7, 22, 9, 7, 31, 7, 5], 18))
