# Greatest Common Divisor
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
