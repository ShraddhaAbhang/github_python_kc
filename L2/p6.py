# wap to read three numbers and find their product

print("enter first number: ")
s1 = input()
n1 = float(s1)

s2 = input("Enter second number: ")
n2 = float(s2)

n3 = float(input("Enter third number: "))

res = n1 * n2 * n3
print("res = ", res)

print("res = ", round(res, 0))
print("res = ", round(res, 1))
print("res = ", round(res, 2))
print("res = ", round(res, 3))
print("res = ", round(res, 4))
print("res = ", round(res, 5))
print("res = ", round(res, 6))


'''
Python Input/Output:

Input:
    - To accept input from keyboard we can use input() funtion which returns string.
    To convert: 
        - String into integer we can use int()
        - String into float we can use float()

Output:
    - To print the output or results Python provides print() funtion
    - print() will print the values and then cursor goes to the next line.

'''