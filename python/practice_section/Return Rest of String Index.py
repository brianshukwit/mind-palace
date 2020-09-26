# Return Rest of String Index
def removeChars(str, n):
    return str[n:]


inputstring = input("Enter string: ")
inputnumber = int(input("Enter index: "))
print(removeChars(inputstring, inputnumber))
