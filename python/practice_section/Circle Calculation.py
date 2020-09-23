# Circle Calculations
PI = 3.141592653589793
radius = float(input('Radius = '))
di = 2 * radius
circ = di * PI
sa = 4 * PI * radius * radius
volume = (4 / 3) * PI * radius * radius * radius

print("Diameter : " + str(di))
print("Circumference : " + str(circ))
print("Surface area : " + str(sa))
print("Volume : " + str(volume))
