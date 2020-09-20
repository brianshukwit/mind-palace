# Code Quiz / Innolitics / Brian Shukwit
import math

i = 0
x = 787878787

while (x > 0):
    if x % 10 == 7:
        i = i + 1
    x = math.floor(x / 10)
    
print('Number of 7s is: ', 1)