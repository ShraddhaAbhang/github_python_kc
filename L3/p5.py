# wapp to read marks between 0 and 100
# marks > 80-->A, 60-->B, 40-->C else D

marks = int(input("Enter marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks > 80:
    print("Grade A")
elif marks > 60:
    print("Grade B")
elif marks > 40:
    print("Grade C")
else:
    print("Grade D")