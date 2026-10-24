# Starting list: numbers = [12, 5, 27, 8, 14, 27, 3]
# Input list: [12, 5, 27, 8, 14, 27, 3]
# Smallest: 3 (at index 6)
# Largest: 27 (at index 2)
# Total: 96
# Average: 13.71
# # Numbers above average: 3

def list_analyser(input):
    smallest = input[0]
    largest = 0
    smallestindex = 0
    largestindex = 0
    total = 0
    count = 0

    for i, num in enumerate(input):
        if num < smallest:
            smallest = num
            smallestindex = i
    for i , num in enumerate(input):
        if num > largest:
            largest = num
            largestindex = i
    for num in input:
        total += num
    
    average = round(total/len(input), 2)

    for x in input:
        if x > average:
            count += 1
    return f"Input: {input}\nSmallest: {smallest} (at index {smallestindex})\nLargest: {largest} (at index {largestindex})\nTotal: {total}\nAvearge: {average}\nNumbers above average: {count}"

    
print(list_analyser([12, 5, 27, 8, 14, 27, 3]))
