# Write a loop that reads positive integer numbers from the user and and count even and odd ones. 
# The loop continues untill presses the Enter key without entering any number.a negative number is entered.
# Your program then prints the result. If the user presses Enter key from the beginning, your code should display
# 'No positive number was entered'.

# The following are sample runs of the program.
# Sample run 1:
# Enter a positive number: (or press Enter key to finish: )
# No positive number was entered.

# Sample run 2:
# Enter a positive number: (or press Enter key to finish: ) 12
# Enter a positive number: (or press Enter key to finish: ) 8
# Enter a positive number: (or press Enter key to finish: ) 15
# Enter a positive number: (or press Enter key to finish: ) 61
# Enter a positive number: (or press Enter key to finish: ) 42
# Enter a positive number: (or press Enter key to finish: )
# You entered 2 odd and 3 even numbers
evenNum = 0
oddNum = 0
num = input("Enter a positive number: (or press Enter key to finish: )")
while num !="":
    value = int(num)
    if value % 2 == 0:
        evenNum +=1
    else:
        oddNum +=1
    num = input("Enter a positive number: (or press Enter key to finish: )")
print(f"You entered {oddNum} odd and {evenNum} even numbers")
        