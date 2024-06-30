# wapp to find the sum of digits
# i/p: 582      o/p: 15
# i/p: 9286     o/p: 25

num = int(input("Enter the num: "))

if num < 0:
    print("Invalid input")
else:
    sum = 0
    digit = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    
    print("Sum = ", sum)

'''
Working:

num = 582
sum = 0
digit = 0

num > 0            digit = num % 10             sum = sum + digit           num = num // 10
582 > 0                 = 582 % 10 = 2             = 0 + 2 = 2                 = 582 // 10 = 58
58 > 0                  = 58 % 10 = 8              = 2 + 8 = 10                = 58 // 10 = 5
5 > 0                   = 5 % 10 = 5               = 10 + 5 = 15               = 5 // 10 = 0
0 > 0
                        print(sum)
                        = 15
                        
'''