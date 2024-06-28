# wapp to read amount in dollars
# and convert into rupees
# if possible print the currency symbol also

dollars = float(input("Enter the dollar: "))

#perform conversion
rupees = dollars * 83

#round off to two digits
dollars = round(dollars, 2)
rupees = round(rupees, 2)

#print answer
print("Dollar: \u00A3", dollars)
print("Rupees: \u20B9", rupees)


# uni code ==> universal code for rupees (\u20B9) and dolar (\u00A3 )


'''
Recap:

Fundamentals:
- COmments ==> #
- Keywords ==> lowercase + None, True, False
- Identifier ==> 4 rules
- Data Types ==> int, float, str and bool
- type() ==> returns the data type of var

Input/Output
input() ==> str
int() ==> str into int
float() ==> str into float
print() ==> print on screen

Operators:
Arithmetic Operators
    + - * / ?? % **
Assignemnt Operators
    = += -= *= /= //+ %= **=
Relational Operators
    == != < <= > >=
Logical Operators
    and or not

'''