# wapp to find the sum of first "n" +ve integer
# i/p: 5        1 + 2 + 3 + 4 + 5 = 15
# i/p: 3        1 + 2 + 3 = 6

num = int(input("Enter +ve number: "))

if num < 0:
    print("Invalid number")
else:
    sum = 0
    i = 1
    while i <= num:
        sum = sum + i
        i = i + 1
    print("sum = ", sum)

'''
Working (looping)

num = 5
sum = 0
i = 1

i <= num        sum = sum + i           i = i + 1
1 <= 5             0 + 1 = 1              1 + 1 = 2
2 <= 5             1 + 2 = 3              2 + 1 = 3
3 <= 5             3 + 3 = 6              3 + 1 = 4
4 <= 5             6 + 4 = 10             4 + 1 = 5
5 <= 5             10 + 5 = 15            5 + 1 = 6
6 <= 5     
                    print(15)

i <= 3          sum = sum + i           i = i + 1
1 <= 3              0 + 1 = 1              1 + 1 = 2
2 <= 3              1 + 2 = 3              2 + 1 = 3
3 <= 3              3 + 3 = 6              3 + 1 = 4
4 <= 3  
                    print(6)

if --> ek baar 
while --> baar baar
'''