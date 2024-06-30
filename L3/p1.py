# wapp to read radius and 
# find the area and circum

radius = float(input("Enter value: "))

if radius < 0:
    print("invalid data")
else:
    pi = 3.14159
    area = pi * radius ** 2
    circum = 2 * pi * radius

    area = round(area,2)
    circum = round(circum,2)


    print("area = ", area)
    print("circum = ", circum)