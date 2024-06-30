# wapp to find the reverse of the number
# i/p: 582          o/p: 285
# i/p: 9286         o/p: 6829

num = int(input("Enter the number: "))

if num < 0:
    print("Invalid number")
else:
    print("num = ", num)

    rev = 0
    digit = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    print("reverse = ", rev)

    '''
    Working:

    num = 123
    rev = 0
    digit = 0

    num > 0             digit = num % 10            rev = rev * 10 + digit              num = num // 10
    123 > 0                 = 123 % 10 = 3              = 0 * 10 + 3 = 3                    = 123 // 10 = 12
    12 > 0                  = 12 % 10 = 2               = 3 * 10 + 2 = 32                   = 12 // 10 = 1
    1 > 0                   = 1 % 10 = 1                = 32 * 10 + 1 = 321                 = 1 // 10 = 0
    0 > 0
                        print = 321
    '''