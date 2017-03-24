import string

def alphabet_position(letter):
    alpha = string.ascii_lowercase
    beta = string.ascii_uppercase
    #find the index of the given letter in the alphabet
    if letter in alpha:
        index = alpha.find(letter)
    else:
        index = beta.find(letter)
    return index


def rotate_character(char, rot):
    alpha = string.ascii_lowercase
    beta = string.ascii_uppercase
    #add the rotation amount to the index of the letter
    if char in string.ascii_lowercase:
        index = alphabet_position(char)
        newindex = (index + rot) % 26
        newchar = alpha[newindex]
    elif char in string.ascii_uppercase:
        index = alphabet_position(char)
        newindex = (index + rot) % 26
        newchar = beta[newindex]
    #if the character is not in the alphabet, pass it through
    else:
        newchar = char
    return newchar

def encrypt(text, rot):
    encryptedtext = ""
    #for each character in the text, rotate the amount specified and add to a new string
    for item in text:
        newtext = rotate_character(item, rot)
        encryptedtext = encryptedtext + newtext
    return encryptedtext
