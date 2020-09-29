# Code Quiz / Innolitics / Brian Shukwit

# string
count_test = 1017717171

# count number of times 7 occurs
count = 0

for i in count_test:
    if i == '7':
        count = count + 1

# print results
print("Number of 7's in the string is: " + str(count))