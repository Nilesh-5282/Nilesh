#code refactoring
def show_help():
    #print the instructions
    print("What should we pick?:")
#have a SHOW command
#Have a HELP command
    print('''Enter'Done' to stop adding the items.
             Enter 'Help' for any help.
             Enter 'Show' to show the item''')
def show_items():
    print("Here's your List")
    for items in shopping_list:
    #print the objects
        print(items)
#make a list to hold the items
shopping_list=[]
show_help()
while True:
#ask for new items
    new_items= input("> ")
    #To quit the app
    if new_items== "Done":
        break
    elif new_items=="Help":
        show_help()
        continue
    #add the items to the list
    elif new_items=="Show":
        show_items()    
    else:
        shopping_list.append(new_items) 
show_items()
