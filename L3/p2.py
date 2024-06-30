# wapp to read length and breadth from user
# and find the area and perimiter of rectengle

lenght = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

if lenght < 0 or breadth < 0:
    print("Invalid data")
else:
    area = lenght * breadth
    perimeter = 2 * (lenght + breadth)

    area = round(area, 2)
    perimeter = round(perimeter, 2)

    print("Area = ", area)
    print("Perimeter: ", perimeter)