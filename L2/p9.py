#wapp to read radius of cicle
#print area and circumference upto 2 digit precision

radius = float(input("Enter the radius: "))

# compute area and circum
area = 3.14159 * radius**2
circum = 2 * 3.14159 * radius

# round off to two digits
area = round(area, 2)
circum = round(circum, 2)

# print the answer
print("Area = ", area)
print("Circum = ", circum)