def main():
    lst = list(range(2,101))   # or lst = []\n  for i in lst: \n \t lst.append(i)
    newList = removing(lst,2)
    newList = removing(lst,3)
    newList = removing(lst,4)
    newList = removing(lst,5)
    print(newList)

def removing(lst , n):
    for j in lst:
        if j % n == 0 and j / n != 1:
            lst.remove(j)
    return lst

if __name__ == "__main__": # This line is optinal مو معانا في المنهج
    main()
    
    