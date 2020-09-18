#Triangle Type
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