# Total Pay
wage = float(input('Enter the Wage: $'))
hours = float(input('Enter the regular hours: '))
overtimeHours = float(input('Enter the overtime hours: '))
regular = hours * wage
overtime = overtimeHours * (wage * 1.5)

total = regular + overtime

print('The total weekly pay is $' + str(total))