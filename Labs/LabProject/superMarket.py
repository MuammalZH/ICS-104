def main():
    projectMenu()
    userChoice = input("Enter your choice: ")
    
    if userChoice == "1":
        productInfo()
        
    elif userChoice == "2":
        searchProduct()
    
    elif userChoice == "3":
        addProduct()
    
    elif userChoice == "4":
        pass
    
    elif userChoice == "5":
        pass
    
    elif userChoice == "6":
        pass
    
    elif userChoice == "7": # To Exit
        pass
    
def projectMenu(): # This is the interface
    numberOfdashes = 31
    print("┌" + "─" * numberOfdashes + "┐") 
    print("│" +" Supermarket Management System " + "│")
    print("└" + "─" * numberOfdashes + "┘")

    print("  1. Print products info")
    print("  2. Search a product")
    print("  3. Add a product")
    print("  4. Remove a product")
    print("  5. Modify a product")
    print("  6. Filter by Price")
    print("  7. Exit")
    print("=" * numberOfdashes) 


def productInfo(): # This function is going to Show all the info of all products(id, name, price, quantity, discount).

    totalProducts = 1
    txtList = []
    csvFile = open("store.txt", "r")
    for line in csvFile:
        wordList = line.split(",")      
        for word in wordList:
            if "\n" in word:         
                totalProducts +=1         # i couldn't use the makingList function because i need to count the total product
                word = word.replace("\n","")
                txtList.append(word)
            else:
                txtList.append(word)

    productID = 0
    productName = 1
    productPrice = 2
    productQuantity = 3
    productDiscount = 4
    print("\n\nTotal", totalProducts,"products:" )
    print("-" * 46) # 46 is the number of dashes no need to define it because i'm only going to use it once
    while True:
        try:
            print("Id:          ", txtList[productID])
            print("title:      ", txtList[productName])
            print("price:      ", txtList[productPrice], "$")
            print("quantity:   ", txtList[productQuantity])
            print("discount:   ", txtList[productDiscount])
            print("-" * 46)
            productID += 5
            productName +=5
            productPrice += 5
            productQuantity += 5
            productDiscount +=5
        except IndexError:
            break
        
        finally:
            csvFile.close()

def searchProduct(): #
    print("\nChoose an option")
    print("=" * 31)
    print("  1. Search by id")
    print("  2. Search by name")
    print("  3. Return to Main Menu")   
    print("=" * 31)

    searchChoice = input("Enter your choice: ")
    txtList = makingList()
    position = 0
    count = 0

    if searchChoice == "1":     
    
        idNumber = input("Enter the id: ") 
        
        for word in txtList:
            word = word.lstrip() # lstrip because there is a space in the left of the inputs i.e [" 123"]
            if word.startswith(str(idNumber)):
                count +=1
        
        print()
        print("Matched products "+ "(" + str(count) + ")") # i make it i string because i don't want any spaces
        print("=" * 31)        
        if count == 0:
            print("This item doesn't exist ")
        
        for word in txtList:
            word = word.lstrip()
            if word == idNumber:
                
                print("Id:          ", txtList[position])
                print("title:      ", txtList[position + 1])
                print("price:       ", float(txtList[position + 2]), "$")
                print("quantity:   ", txtList[position + 3])
                print("discount:   ", txtList[position + 4])
                print("-" * 46)
                break
            else:
                position +=1
    elif searchChoice == "2": # it is smilar to searchChoice "1"

        nameOftheProduct = input("Enter the name: ")
               
        for word in txtList:
            word = word.lstrip()
            if word.startswith(nameOftheProduct):
                count +=1
            
        print()
        print("Matched products "+ "(" + str(count) + ")")
        print("=" * 31)
        if count == 0:
            print("This item doesn't exist ")
            
        for word in txtList:
            word = word.lstrip()
            if word.startswith(nameOftheProduct):
            
                print("Id:          ", txtList[position -1])
                print("title:      ", txtList[position])
                print("price:       ", float(txtList[position + 1]), "$") # it is a float in the sample run
                print("quantity:   ", txtList[position + 2])
                print("discount:   ", txtList[position + 3])
                print("-" * 46)
                
            position +=1
        
    elif searchChoice == "3":
        main() # return to the main menu
                
                
def addProduct(): # This function is going to add a new product in the txt file

    addingProduct = []
    csvFile = open("store.txt", "r")
    for line in csvFile:
        wordList = line.split(",")      # i cannot use makingList function because i need the \n
        for word in wordList:
            addingProduct.append(word)


    productID = input("Enter id: ")

    count = 0

    for word in addingProduct:
        word = word.lstrip() # lstrip because there is a space in the left of the inputs i.e [" 123"]
        if word.startswith(str(productID)):
            count +=1 # o know if the item is already in the file or not
            

    if count == 0:
        addingProduct.append("\n") 
        addingProduct.append(productID)
        addingProduct.append(" ")

        productName = input("Enter name: ")
        addingProduct.append(productName)
        addingProduct.append(" ")


        productPrice = input("Enter price: ")
        addingProduct.append(productPrice)
        addingProduct.append(" ")

        productQuantity = input("Enter quantity: ")
        addingProduct.append(productQuantity)
        addingProduct.append(" ")

        productDiscount = input("Enter discount: ")
        addingProduct.append(productDiscount)

        print("New product was added successfully")

        storeFile = open("store.txt" , "w")

        for word in addingProduct:
            word = word.replace(" ",", ")
            storeFile.write(word) # to write all the file again because when i opened it everything will be erased
            
        storeFile.close()      
    
    
    else:
        productQuantity = int(input("Enter quantity: "))
        index = 0
        for id in addingProduct:
            if id == productID:
                oldQuan = addingProduct.pop(index + 3) # + 3 is the position of the quantity
                sumOfQuantity = " " + str(int(oldQuan) + productQuantity) 
                addingProduct.insert(index + 3 ,sumOfQuantity )
            else:
                index +=1
        storeFile = open("store.txt" , "w")

        for word in addingProduct:
            word = word.replace(" ",", ")
            storeFile.write(word) # to write all the file again because when i opened it everything will be erased
            
        storeFile.close()   
       
    
                
def makingList(): #This function is going to create a list from the txt file 
    txtList = []
    csvFile = open("store.txt", "r")  # csv = comma separated values
    for line in csvFile: 
        wordList = line.split(",")   # comma between everything
        for word in wordList: # for each word
            if "\n" in word: # remove \n because it will cause a trouble in the printing latter
                word = word.replace("\n","")
                txtList.append(word)
            else: # to deal with each word separately
                txtList.append(word)
    return(txtList)   # return the list



if __name__ == "__main__":
    main()