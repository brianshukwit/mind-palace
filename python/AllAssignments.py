# All Assignments done by me in my Intergrative Programming class
# ////////////////////////////////////////////////////////////////////////// 1.5
base = float(input("Enter the base: "))
height = float(input("Enter the height: "))
area = 0.5 * base * height
print("The area is", area, "square units.")
# /////////////////////////////////////////////////////////////////////////1.6
PI = 3.14
radius = float(input ("Input the radius of the circle: "))
area = PI * radius * radius
print ("Area: %.2f" %area)
# /////////////////////////////////////////////////////////////////////////1.7
name = input("Enter your name: ")
age = input("Enter your age: ")
print(name + " is " + age + " years old.")
# //////////////////////////////////////////////////////////////////////////2.1
TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
               
# Request the inputs
grossIncome = float(input("Enter the gross income: "))
numDependents = int(input("Enter the number of dependents: "))   

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - \
                DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
         
# Display the income tax
print("The income tax is $" + str(round(incomeTax, 2)))
# ///////////////////////////////////////////////////////////////////////////////2.4
PI = 3.141592653589793
radius = float(input('Radius = '))
di = 2 * radius
circ = di * PI
sa = 4 * PI * radius * radius
volume = (4 / 3) * PI * radius * radius * radius

print("Diameter : " + str(di))
print("Circumference : " + str(circ))
print("Surface area : " + str(sa))
print("Volume : " + str(volume))
# ///////////////////////////////////////////////////////////////////////////////2.6
mass = float(input("Enter the object's mass: ")) 
velocity = float(input("Enter the object's velocity: "))  

# Compute the results
momentum = mass * velocity
KE = 0.5 * mass * velocity**2

# Display the results
print("The object's momentum is", momentum)
print("The object's kinetic energy is", KE)
# ///////////////////////////////////////////////////////////////////////////////2.8
seconds = 365 * 24 * 60**2

rate = 3 * 10**8

lightyear = rate * seconds

print("Light travels " + str(lightyear) + " meters in a year")
# ///////////////////////////////////////////////////////////////////////////////2.10
wage = float(input('Enter the Wage: $'))
hours = float(input('Enter the regular hours: '))
overtimeHours = float(input('Enter the overtime hours: '))
regular = hours * wage
overtime = overtimeHours * (wage * 1.5)

total = regular + overtime

print('The total weekly pay is $' + str(total))
# ///////////////////////////////////////////////////////////////////////////////3.2
first = int(input("Enter the first side: "))
second = int(input("Enter the second side: "))
third = int(input("Enter the third side: "))

if (first**2 + second**2) == third**2:
    print("The triangle is a right triangle.")
elif (first**2 + third**2) == second**2:
    print("The triangle is a right triangle.")
elif (second**2 + third**2) == first**2:
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")
# ///////////////////////////////////////////////////////////////////////////////3.8
num1 = float(input(" Please Enter the First Value  Num1 : "))
num2 = float(input(" Please Enter the Second Value Num2 : "))

a = num1
b = num2

while(num2 != 0):
    temp = num2
    num2 = num1 % num2
    num1 = temp

gcd = num1   
print("\n The greatest common divisor is {2}".format(a, b, gcd))
# ///////////////////////////////////////////////////////////////////////////////4.1
plainText = input("Enter a message: ") 
distance = int(input("Enter the distance value: ")) 
code = "" 
for ch in plainText:    
    ordValue = ord(ch)  
    cipherValue = ordValue + distance   
    if cipherValue > ord('z'):      
        cipherValue = ord('a') + distance - (ord('z') - ordValue + 1)
    code = code + chr(cipherValue)
print(code)	
# ///////////////////////////////////////////////////////////////////////////////4.2
def decrypt():
    ciphertext = input("Enter your coded text: ")
    shift = int(input("Enter the distance value: "))
    space = []

    # creat a list of encrypted words.
    ciphertext = ciphertext.split()

    # creat a list to hold decrypted words.
    sentence = []

    for word in ciphertext:
        cipher_ords = [ord(x) for x in word]
        plaintext_ords = [o - shift for o in cipher_ords]
        plaintext_chars = [chr(i) for i in plaintext_ords]
        plaintext = ''.join(plaintext_chars)
        sentence.append(plaintext)

    sentence = ' '.join(sentence)
    
    print(str(sentence))
    
decrypt()
# ///////////////////////////////////////////////////////////////////////////////4.4
bstring = input("Enter a string of bits: ")
decimal = 0
exponent = len(bstring) - 1
for digit in bstring:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)

decimal = int(input("Enter a decimal integer: "))
if decimal == 0: 
    print(0)
else:
    print("Quotient Remainder Binary")
    bstring = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bstring = str(remainder) + bstring
        print("%5d%8d%12s" % (decimal, remainder, bstring))
    print("The binary representation is", bstring)  
	
print("Enter 'x' for exit.");
dec = input("Enter number in Decimal Format: ");
if dec == 'x':
    exit();
else:
    decimal = int(dec);
    print(decimal,"in Octal =",oct(decimal));

print("Enter 'x' for exit.");
octal = input("Enter number in Octal Format: ");
if octal == 'x':
    exit();
else:
    decimal = str(int(octal, 8));
    print(octal,"in Decimal =",decimal);	
# ///////////////////////////////////////////////////////////////////////////////4.5
bits = input("Enter a string of bits: ")
bits = bits[1:] + bits[0]
print("Result:", bits)

bits = input("Enter a string of bits: ")
bits = bits[-1] + bits[:-1]
print("Result:", bits)
# ///////////////////////////////////////////////////////////////////////////////4.8
filename1 = input("Enter the input file name: ")
filename2 = input("Enter the output file name: ")
file1 = open(filename1)
file2 = open(filename2, 'w')
file2.writelines(file1)
file2.close()
file1.close()
# ///////////////////////////////////////////////////////////////////////////////5.2
enterfile = input("Enter the file name: ")
file = open(enterfile, 'r')
linecount = 0

for line in file:
    linecount = linecount + 1

print("The number of lines in this txt. file is", linecount)

while True:
    linenum = 0

    num = int(input("Please enter a line number or press 0 to quit: "))
    if num >=1 and num <= linecount:
        file = open(enterfile, 'r')
        for lines in file:
            linenum = linenum + 1
            if linenum == num:
                print(lines)
    else:
        if num == 0:
            print("Thanks for using the program")
            break
# ///////////////////////////////////////////////////////////////////////////////5.7
my_str = open(input("Enter: "), "r").read().split()

my_str.sort()

# display the sorted words

print("The sorted words are:")
for word in my_str:
   print(my_str)
 # ///////////////////////////////////////////////////////////////////////////////5.8
f = open(input("Enter: "), "r").read()
myDict = {}
linenum = 0

for word in f.split():
    if not word in myDict:
        myDict[word] = []

    myDict[word].append(linenum)


print("%-15s %-15s" %("Word", "Frequency"))
for key in sorted(myDict):
    print('%-15s: %-15d' % (key, len(myDict[key])))
 # /////////////////////////////////////////////////////////////////////////////// 6.6
 import os, os.path

QUIT = '8'

COMMANDS = ('1', '2', '3', '4', '5', '6', '7', '8')

MENU = """1   List the current directory
2   Move up
3   Move down
4   Number of files in the directory
5   Size of the directory in bytes
6   Search for a file name
7   View the contents of a file
8   Quit the program"""

def main():
    while True:
        print(os.getcwd())
        print(MENU)
        command = acceptCommand()
        runCommand(command)
        if command == QUIT:
            print("Have a nice day!")
            break

def acceptCommand():
    """Inputs and returns a legitimate command number."""
    while True:
        command = input("Enter a number: ")
        if not command in COMMANDS:
            print("Error: command not recognized")
        else:
            return command

def runCommand(command):
    """Selects and runs a command."""
    if command == '1':
        listCurrentDir(os.getcwd())
    elif command == '2':
        moveUp()
    elif command == '3':
        moveDown(os.getcwd())
    elif command == '4':
        print("The total number of files is", \
              countFiles(os.getcwd()))
    elif command == '5':
        print("The total number of bytes is", \
              countBytes(os.getcwd()))
    elif command == '6':
        target = raw_input("Enter the search string: ")
        fileList = findFiles(target, os.getcwd())
        if not fileList:
            print("String not found")
        else:
            for f in fileList:
                print(f)
    elif command == '7':
            viewFile(os.getcwd())

def viewFile(dirName):
    lyst = list(filter(os.path.isfile, os.listdir(dirName)))
    if len(lyst) == 0:
        print("No files - have a good day")
    else :
        while True:
            print("Files in " + dirName + ":")
            break
    for element in lyst: print(element)
    fileName = input("Enter a file name for these names: ")
    if not fileName in lyst:
        print("Sorry that's wrong...")
    else :
        f = open(fileName, 'r')

    print(f.read())
    


def listCurrentDir(dirName):
    """Prints a list of the cwd's contents."""
    lyst = os.listdir(dirName)
    for element in lyst: print(element)

def moveUp():
    """Moves up to the parent directory."""
    os.chdir("..")

def moveDown(currentDir):
    """Moves down to the named subdirectory if it exists."""
    newDir = input("Enter the directory name: ")
    if os.path.exists(currentDir + os.sep + newDir) and \
       os.path.isdir(newDir):
        os.chdir(newDir)
    else:
        print("ERROR: no such name")

def countFiles(path):
    """Returns the number of files in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += countFiles(os.getcwd())
            os.chdir("..")
    return count

def countBytes(path):
    """Returns the number of bytes in the cwd and
    all its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += countBytes(os.getcwd())
            os.chdir("..")
    return count

def findFiles(target, path):
    """Returns a list of the file names that contain
    the target string in the cwd and all its subdirectories."""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if target in element:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(findFiles(target, os.getcwd()))
            os.chdir("..")
    return files

if __name__ == "__main__":
    main()
	
 # /////////////////////////////////////////////////////////////////////////////// 9.1
class Student(object):
    """Represents a student."""

    def __init__(self, name, number):
        """All scores are initially 0."""
        self.name = name
        self.scores = []
        for count in range(number):
            self.scores.append(0)

    def getName(self):
        """Returns the student's name."""
        return self.name
  
    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self.scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self.scores[i - 1]
   
    def getAverage(self):
        """Returns the average score."""
        return sum(self.scores) / len(self._scores)
    
    def getHighScore(self):
        """Returns the highest score."""
        return max(self.scores)
 
    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self.name  + "\nScores: " + \
               " ".join(map(str, self.scores))
        
    def __eq__(self, other):

        if self is other: 
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.name == other.name
    
    def __lt__(self, other):

        return self.name < other.name
    
    def __ge__(self, other):

        return self.name >= other.name

def main():
    """A simple test."""
    student = Student("Ken", 5)
    print(student)
    for i in range(1, 6):
        student.setScore(i, 100)
    print(student)
    
    s2 = Student("Ben",7)
    print(s2)
    for i in range(1,6):
        student.setScore(i,98)
    print(student)

    
    

if __name__ == "__main__":
    main()
	
 # /////////////////////////////////////////////////////////////////////////////// 4.11
 import re
# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
text = inputFile.read()

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

# Count the words
words = len(text.split())

# Count the syllables
syllables = 0
vowels = "aeiouAEIOU"
for word in text.split():
    syllables += len(re.findall('[aeiouAEIOU]+', word))        
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1
    


# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / sentences) - \
        84.6 * (syllables / words)
level = int(round(0.39 * (words / sentences) + 11.8 * \
                  (syllables / words) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables") 
 # /////////////////////////////////////////////////////////////////////////////// 6.9
 
import functools
def sum(x,y):
    return x+y

def main():
    fname = input("Enter filename:")
    infile = open(fname, "r")
    
    total = 0
    num_of_entries = 0
    lines = infile.readlines()
    
    
       
    for line in lines:
        nums = list(map(int, line.split()))
        num_of_entries += len(nums)
        total += functools.reduce(sum, nums)
        
    

    
    average = total/num_of_entries
    
    print(average) 

main()
