# Determine whether a string contains balanced brackets. Every opening bracket must have a matching closing bracket of the same type in the correct order. Handle round (), square [], and curly {} brackets.
# Examples
# Input: "(a + b) * [c - d]" → Balanced
# Input: "(a + b)]" → Not balanced (mismatched type)
# Input: "((a + b)" → Not balanced (unclosed)
# Input: "[(a + b) * {c - d}]" → Balanced
# Input: "([)]" → Not balanced (wrong order)

def balance_parantenses(input):
    found = []
    for char in input:
        if char == "(" or char == "[" or char == "{":
            found.append(char)
    
        if char == ")" or char == "]" or char == "}":
            check = found.pop()
            if check == "(" and char !=  ")" or check == "{" and char != "}" or check == "[" and char != "]":
                return "Not balanced"

    if len(found) < 1:
        return "Balanced"
    else: 
        return "Not balanced"

print(balance_parantenses("[(a + b) * {c - d}]"))



