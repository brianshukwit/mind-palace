# Number Decimal Octal
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
    print(decimal, "in Octal =", oct(decimal));

print("Enter 'x' for exit.");
octal = input("Enter number in Octal Format: ");
if octal == 'x':
    exit();
else:
    decimal = str(int(octal, 8));
    print(octal, "in Decimal =", decimal);