
def main():
    gpa = float(input("What is your GPA : "))
    if gpa > 0 and gpa <= 4 :
        credit = int(input("How many credit do you have? :  "))
        if credit >= 12 :
            if credit == 12 and gpa == 4 :
                thirdHonor()
            elif credit == 13 and gpa >= 3.692:
                thirdHonor() 
            elif credit == 14 :
                if gpa == 4 :
                    secondHonor()
                elif gpa >= 3.428 and gpa <= 3.990:
                    thirdHonor()
            elif credit == 15 :
                if gpa == 4:
                    firstHonor()
                elif gpa >= 3.733 and gpa <= 3.990:
                    secondHonor()
                elif gpa >= 3.200 and gpa <= 3.733:
                    thirdHonor()
            elif credit >= 16:
                if gpa >= 3.750 :
                    firstHonor() 
                elif gpa >= 3.500 and gpa <= 3.740:
                    secondHonor()   
                elif gpa >= 3.000 and gpa <= 3.490:
                    thirdHonor()
            else:
                print("Not Eligible For Honor")        

        else:
            print("Not Eligible For Honor")
    else:
        print("Invalid GPA")    


def thirdHonor():
    print("Third Class Honor\n500SAR")

def secondHonor():
    print("Second Class Honor\n750SAR")

def firstHonor():
    print("First Class Honor\n1000SAR")

if __name__ == "__main__":
    main()