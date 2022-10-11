# using while loop, write a program that reads from the user the value of an integer number n 
# (has to be positive and multiple of 5). Then your program finds and displays the sum of multiples of 5 from 5 to n i.e.
# sum=5+10+15+20+……..+n
# If the user enters wrong input, your program displays “Wrong input” message.
# Sample runs are shown below:
# Enter n ( >0 and muliple of 5 ): -10
# Wrong input

# Enter n ( >0 and muliple of 5 ): 11
# Wrong input

# Enter n ( >0 and muliple of 5 ): 25
# Sum = 75
 # 15 == 5 + 10 + 15
n = int(input("Enter n ( >0 and muliple of 5 ): "))
sum = 0
i = 5
if n >= 0 and n % 5 == 0:
    while i <= n:
        sum += i
        i = i +5        
    print(sum)        
else:
    print("Wrong input")
    