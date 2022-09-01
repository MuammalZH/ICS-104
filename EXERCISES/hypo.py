import math # it is not necessary if i did what i write in the comment ol line 8
# write a program that computes the hypotenuse of a right triangle

opposite = int(input("Enter the opposite: "))
adjacent = int(input("Enter the adjacent: "))
# by Pythagoras Theorem
firstStep = opposite**2 + adjacent**2
hypotenuse = math.sqrt(firstStep) # i can also write firstStep **(1/2)
print(hypotenuse)






