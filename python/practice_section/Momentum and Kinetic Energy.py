# Momentum and Kinetic Energy
mass = float(input("Enter the object's mass: ")) 
velocity = float(input("Enter the object's velocity: "))  

# Compute the results
momentum = mass * velocity
KE = 0.5 * mass * velocity**2

# Display the results
print("The object's momentum is", momentum)
print("The object's kinetic energy is", KE)
