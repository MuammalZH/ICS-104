#Write a program the computes the distance between two points 
# d=√((x_2-x_1)²+(y_2-y_1)²)
import math
x1 = float(input("What is the first x: "))
y1 = float(input("What is the first y: "))
x2 = float(input("What is the second x: "))
y2 = float(input("What is the Second y: "))
firstStep = abs(y2 - y1)**2
secondStep = abs(x2 - x1)**2
thirdStep =math.sqrt(firstStep+secondStep)
answer = round(thirdStep, 2)
print("The distance is: ",answer)