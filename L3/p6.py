# wapp to read the age of the user (5 to 110)
# advice them age appr vahicle
# age 5 and 18--> cycle         # age 19 and 25--> bike
# age 26 and 35--> car          # above 35 sedan

age = int(input("Enter the age: "))

if age < 5 or age > 110:
    print("Invalid age")
elif age >= 5 and age <= 18:
    print("Cycle")
elif age >= 19 and age <= 25:
    print("Bike")
elif age >= 26 and age <= 35:
    print("Car")
else:
    print("Sedan")

