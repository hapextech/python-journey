input = "aaabbc"

def length_encoding(input):
    output = ""
    count = 1
    for i, char in enumerate(input):
        if (i + 1) < len(input) and char == input[i+1]:
            count += 1
        else:
            output += char + str(count)
            count = 1


    return output

print(length_encoding("aaabbc"))