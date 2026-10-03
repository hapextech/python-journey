#  Word Frequency

# Problem
# Given a paragraph of text, count how many times each word appears and store it in a dictionary. Then, find and print the single most frequent word. 
# Examples
# Input: "Python is fun, and Python is powerful!"
# Output: Most frequent word: python (2) 

# Constraints
# Treat uppercase and lowercase as the same.
# You must strip basic punctuation (like commas and periods) manually without using the re module or string.punctuation.
# After counting, you must find the most frequent word without using max() or sorting the dictionary.
# Do not use collections.Counter. 

# firstly i want to split the items 
# in the string by the space
Input = "Python is fun, and Python is powerful!".split()
dic = {}

# print(Input)

# i want to remove all the punctuations in each item.
for x in range(len(Input)):
    res = ""
    for char in Input[x]:
        if char.isalnum():
            res += char
        Input[x] = res
# print(Input)

    
# i want to save the items in my list 
# in my empty dic by key 
# and value as num of time they appeared
for key in Input:
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1
# print(dic)

# finding the higest value in the dic
highest = 0
for keys in dic:
    if dic[keys] > highest:
        highest = dic[keys]
print(highest)

# printing the key with the highest value 
print("Frequent word: ")
for x in dic:
    if dic[x] == highest:
        print(f"{x}: {dic[x]}  ")