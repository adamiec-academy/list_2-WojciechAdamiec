def cipher(text, shift):
    result = ""

    for letter in text:
        if letter == " ":
            result += letter
        elif letter.isupper():
            result += chr((ord(letter) + shift -65) % 26 + 65)
        else:
            result += chr((ord(letter) + shift - 97) % 26 + 97)
 
    return result


def decipher(text, shift):
    return cipher(text, -shift)
