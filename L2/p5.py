"""
Python Fundamentals

Python Comments: (#)
    Comments are any text to the right of # symbol and is mainly uselful as notes for the reader of the program.

    Comments explain:
        - Assumptions
        - Important decision
        - Important details
        - Problems you're trying to solve

Python Keywords:

Python uses keywords to recognize the structure of the program and hence they cannot used for any other prupose.

"""


"""
Identifier:
    Identifier is a name given to programmung element like variables, funtions, strings, etc.

    Indentifier rules:
        - Name can contain any combinations of letters, _ and digits. ==> and = 20  (SyntaxError: Invalid syntax)
        - NAME CANNOT BEGIN WITH DIGIT. ==> 1abc = 20   (SyntaxError: Invalid syntax)
        - Name are case - sensitive. ==> _abc = 20   (OK)
        - Keywords cannot be used identifier ==> _=20   (OK)

Data Types:
    Python has following data types:
        - Numbers - int, float
        - Boolean - bool
        - String - str
        - Tuple - tuple
        - List -list
        - Dictionary - dict

    Note: 
        - Python does not have char datatype
        - Python does not support any constant declaration

"""

a = 10
print(a, type(a))

b = 345
print(b, type(b))

c = 3.4
print(c, type(c))

d = 2e3
print(d, type(d))

e = "Hello Git"
print(e, type(e))

f = "Hello Git India"
print(f, type(f))

g = True
print(g, type(g))

h = False
print(h, type(h))

i = "true"
print(i, type(i))

