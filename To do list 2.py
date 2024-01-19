#Maille Retzloff
#To-Do List 2
items = [" "]
  
def ListMenu():
    print("Welcome to the List Menu")
    print("Please choose an operation: (type in a number between 1 - 5)")
    print( "1. Add to List \n2. View List \n3. Mark Item Completed  \n4. Remove an Item \n5. Remove All Items \n6. Sort List Alphabetically \n7. Print Number of Items on List \n8. Quit the Program")
    option = int(input("Option: "))

    if option == 1:
        food = (input ("what item would you like to add to the list? "))
        items.insert(0,food)
        ListMenu()
        
    if option == 2:
        print(items)
        ListMenu()

    if option == 3:
        food = (input("What item have you bought?"))
        number = int(input("Input position on list - first item is position 0"))
        items[number] = "X " + food
        ListMenu()
    
    if option == 4:
        food = (input("what item would you like to remove from the list? "))
        items.remove(food)
        ListMenu()
    
    if option == 5:
        items.clear()
        print(items)
        ListMenu()
    
    if option == 6:
        items.sort()
        print(items)
        ListMenu()
    
    if option == 7:
        print(len(items))
        ListMenu()

    if option == 8:
        quit()

ListMenu()