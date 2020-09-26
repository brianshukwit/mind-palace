# Print Even Index
def printEvenIndexChar(str):
  for i in range(0, len(str)-1, 2):
    print(str[i])


inputStr = "For Frodo!"
print("Orginal String is ", inputStr)

print("Printing only even index chars")
printEvenIndexChar(inputStr)