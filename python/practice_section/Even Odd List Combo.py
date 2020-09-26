# Even Odd List Combo
list1 = [1,22,3,46]
list2 = [55,6,73,88]

newlist = list1 + list2
odd_i = []
even_i = []
for i in range(0, len(newlist)):
    if i % 2:
        even_i.append(newlist[i])
    else:
        odd_i.append(newlist[i])

result = odd_i + even_i

print(result)
