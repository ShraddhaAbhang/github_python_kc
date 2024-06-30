# wapp to read year and find if its
# a leap year
# it comes after every 4 years
# it is multiple of 4 / divisible by 4

year = int(input("Enter the year: "))

if year % 4 == 0:
    print("Yes, it is a leap year")

else:
    print("No, its not a leap year")
