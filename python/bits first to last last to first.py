# bits first to last last to first
bits = input("Enter a string of bits: ")
bits = bits[1:] + bits[0]
print("Result:", bits)

bits = input("Enter a string of bits: ")
bits = bits[-1] + bits[:-1]
print("Result:", bits)