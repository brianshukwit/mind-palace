def product_function(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

number1 = int(input("First Number: "))
number2 = int(input("Second Number: "))

result = product_function(number1, number2)
print("The result is", result)