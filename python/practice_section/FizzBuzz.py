def findDivisible(numberList):
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        if num % 5 == 0:
            print("Fizz")
        if num % 3 == 0:
            print("Buzz")
        if num % 5 == 0 and num % 3 == 0:
            print("FizzBuzz")


numList = [10, 20, 33, 45, 55, 15]
findDivisible(numList)