# Using for loop, write a python program that reads an integer from the user and prints back 
# the number of the digits in that integer and the sum of them. For example,
# if the input was 2308 , the output would be: Your integer has 4 digits and their sum is 13.

# Hint: take your input as a string and use for loop to get the digits.
# The following are sample runs of the program:

# Sample run 1:*
# Enter a positive integer value: 2308
# Your integer has 4 digits and their sum is 13

# Sample run 2:*
# Enter a positive integer value: 714702
# Your integer has 6 digits and their sum is 21

num = input(" Enter a positive integer value: ")
n = 0
total = 0
digits = int(num)
numOfDigits = 0
for idx in num:
    total += int(num[n])
    if digits // 10 != 0:
        numOfDigits += 1
        
    n += 1
print(f"Your integer has {numOfDigits} digits and their sum is {total} ")


    