# Caesar Cipher
# Problem
# Build a program that can encrypt and decrypt a message by shifting letters by a given number. For example, a shift of 1 makes 'a' become 'b', and 'z' becomes 'a'.  
# Examples
# Input: Text: hello | Shift: 1 | Mode: encrypt → Output: ifmmp
# Input: Text: xyz | Shift: 2 | Mode: encrypt → Output: zab (Notice the wrap-around)
# Input: Text: hello, world! | Shift: 3 | Mode: encrypt → Output: khoor, zruog! (Notice punctuation and spaces are preserved)
# Input: Text: ifmmp | Shift: 1 | Mode: decrypt → Output: hello 
# Constraints
# Must handle alphabetical wrap-around correctly (e.g., 'z' shifted by 1 becomes 'a', 'a' shifted backward by 1 becomes 'z').
# Must preserve spaces, numbers, and punctuation without shifting or altering them.
# The program must ask the user if they want to encrypt or decrypt.
# Do not use external libraries (like cryptography). 

def caesar(word, shift, mode):

    word = word.strip().lower()
    res = ""
    punctuation = " ,?!"

    for char in word:
        if char in punctuation:
            res += char
            continue

        if mode == "encrpyt":
            res += chr((ord(char) - 97 + shift) % 26 + 97)
        elif mode == "decrpyt":
            res += chr((ord(char) - 97 - shift) % 26 + 97)
    return res

print(caesar("ifmmp", 1, "decrpyt"))


