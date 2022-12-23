def censor(text):
    result = ""
    for letter in text:
        if "0" <= letter <= "9":
            result += "*"
        else:
            result += letter
    return result
