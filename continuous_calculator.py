# . Simple Calculator
# Problem
# Build a continuous calculator that maintains a running total. The user inputs an operator and a number repeatedly (e.g., + 5, then * 2). 
# Examples
# Input: + 5 → Result: 5
# Input: * 2 → Result: 10
# Input: undo → Result: 5 
# Constraints
# Must handle floating-point numbers.
# Implement an undo feature that reverts the calculation to the previous state.
# Strictly forbid the use of eval().
# Must handle division by zero and invalid operators without crashing the program.
# Do not import libraries.

def simple_calculator(num1, operator, num2):
    if operator == "-":
        return num1 - num2
    elif operator == "+":
        return num1 + num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Not divisible by Zero"
        else:
            return num1 / num2
    else:
        "Invalid operator"
# print(simple_calculator(1, "/", 0))

result = 0.0
prev_num = [0.0]

while True:
    user_input = input("Input: ").strip().lower()
    if len(prev_num) > 1 and user_input == "undo":
        prev_num.pop()
        print(prev_num[-1])
        continue

    try:
        operator, num = user_input.split()
        result =  simple_calculator(result, operator, float(num))
        print("result: ", result)

        if isinstance(result, float):
            prev_num.append(result)
        else:
            result = prev_num[-1]
    except: 
        print("Wrong input format. (eg: + 4)")
        continue