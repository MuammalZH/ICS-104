# Question 1: Logic Functions Calculator
# I will use the camelCase
logicName = input("Enter logic function name (and, or, not): ").lower().strip() # i used the lower and strip methods to ignore the user errors
firstValue = int(input("Enter value of condition A: ")) # This is the value of condition A
secondValue = int(input("Enter value of condition A: ")) # This is the value of condition B

# The second step is to validate the function names.
if logicName == "and" :
    pass

elif logicName == "or" :
    pass

elif logicName == "not" :
    pass

else:
    print("Error: unknown logic function")