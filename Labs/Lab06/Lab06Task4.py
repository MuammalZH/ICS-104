# Write a program that prompts for and reads the number  𝑛  >=3 . If  𝑛<3  
# your program must display an error message and terminate; otherwise, using for loop,
# it prints all numbers between 1 and n that are divisible by either 3 or 5 on the same line:

# The following are sample runs of the program.

# Enter n ( >=3 ): 2
# Wrong input n must be >= 3

# Enter n ( >=3 ): 27
# numbers between 1 and 27 divisible by 3 or 5 are:
# 3 5 6 9 10 12 15 18 20 21 24 25 27

n = int(input("Enter n ( >=3 ): "))
sum = 0
if n >= 3:
    print("numbers between 1 and 27 divisible by 3 or 5 are:")
    for i in range(3,n+1):
        if i % 3 == 0 or i % 5 == 0:
            print(i,end = " ")
else:
    print( "Wrong input n must be >= 3")

