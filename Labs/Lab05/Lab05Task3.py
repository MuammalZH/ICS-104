month = int(input("Enter a month:"))
if month >= 1 and month <= 12:
    if month in [1,3,5,7,8,9,12]:
        print("31 days")
    elif month in [4,6,9,11]:
        print("30 days")
    elif month == 2:
        print("28 or 29 days")
else:
    print("Wrong input")