# Write a program that prompts the user to enter five test scores and then prints the  average test score. (Assume that the test scores are decimal numbers.
def main():
    x = 1
    scoreTest = 0
    while x <= 5: # or i can do for i in range(5)
        userInput = float(input(f"Inter your {x} score: "))
        x += 1
        scoreTest += userInput

    print("Your Average is: ", scoreTest/5)    
    return scoreTest
if __name__ == "__main__":
    main()
