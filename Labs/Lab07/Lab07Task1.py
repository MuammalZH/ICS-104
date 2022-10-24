alphabet='abcdefghijklmnopqrstuvwxyz'
numberOfLines = int(input("Enter number of lines to generate: "))
index = numberOfLines

for i in range(numberOfLines):
    for j in range(numberOfLines - i):
        print(numberOfLines , index , end = "-- ")      
    index -=1
    print()
