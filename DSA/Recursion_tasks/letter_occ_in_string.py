def letters(text, count=0):
    if count >= len(text):
        return ""
    else:
        if count <= len(text)-2 and text[count:count+2] == "pi":
            return "3.14" + letters(text, count+2)
        else:
            return text[count] + letters(text, count+1)


text = input()
print(letters(text))