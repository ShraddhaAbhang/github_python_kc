# wapp to check if the given interger is even or odd
# even numbers ==> multiple of 2 / divisible by 2 eg. 0, 2, 4, 6, 8, 20,...

num = int(input("Enter any integer: "))


#---Logic 1
res = num % 2

if res == 0 :
    print("Even")

else:
    print("Odd")

    
#---Logic 2
if num % 2 == 0:
    print("Even")
else:
    print("Odd")



'''
Python Operators:

    Arithmetic Operators:
        +   Addition
        -   Substraction
        *   Multiplication
        /   Division
        //  Floor Division          --division operatands where result is quotient in which digits are removed after decimal point
        %   Modulus
        **  Exponent

'''

'''
Order of Operations:

-When more than one operator appears in expression Python follows P E M D A S. (Perenthesis, Exponent, Multiply, Division, Addition, Substraction)
-Operators with same precedence are evaluated left to ro=ight. (expect Exponent operator which is right to left)

'''