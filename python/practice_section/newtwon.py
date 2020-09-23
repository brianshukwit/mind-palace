import math

tolerance = 0.000001
estimate = 1.0

def newton(x):
    """ Returns the square root of x """
    #Performs the successive approximations

    while True:
        estimate = ((estimate + x / estimate) / 2)
        difference = abs(x - estimate ** 2)
        if difference <= tolerance:
            break           
    return estimate

def main():
    
    while True:
        
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":     
            break       
        x = float(x)
        print("The program's estimate is ", x)
        print("Python's estimate is: ", math.sqrt(x))
main()
