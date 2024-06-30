# wapp to read two integers and find the min of 2

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))


# logic 1
if n1 < n2:
    print("Minimum = ", n1)
else:
    print("Minimum: ", n2)

# logic 2

print("Minimum: ", min(n1, n2))