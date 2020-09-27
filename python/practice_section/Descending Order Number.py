# Descending Order Number
def descending_order(num):
    return int("".join(sorted(str(num),reverse=True)))


newNumber = descending_order(13566)
print(newNumber)