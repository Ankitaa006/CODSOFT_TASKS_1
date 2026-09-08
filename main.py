# Declare empty way
todoList = []

# Function to add new task
def addTask():
    task = input("Enter a task: ")
    todoList.append({"Task": task, "Status":"pending"})
    print("New Task Added Successfuly!\n")
    
# Function to view All Task
def viewTask():
    print("Your To Do List")
    if len(todoList) == 0:
        print("No pending tasks!")
    else:
        # Enumurate add a counter to an iterable(inbuild)
        for index, task in enumerate(todoList, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")
    

# function for remove Task

def removeTask():
    if len(todoList) == 0:
        print("List is empty.")
        
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todoList):
                removeedTask = todoList.pop(search_index)
                print(f"Task removed is: {removeedTask['Task']}")
            else:
                print("invalid Task Number.")
                
        except ValueError:
            print("Please enter valid task number")
        

# mark as complete
def MarkComplete():
    if len(todoList) == 0:
        print("List is empty.")
        
    else:
        try:
            search_index = int(input("Enter the task number that you want to mark as complete: ")) - 1
            if 0 <= search_index < len(todoList):
                todoList[search_index]['Status'] = "Complete"
                print(f"Task : Task {todoList[search_index]['Task']} has been marked as complete.")
            else:
                print("invalid Task Number.")
                
        except ValueError:
            print("Please enter valid task number")
    
    
#function to display menu
def displayMenu():
    while True:
        # exec("cls")
        print("Main Menu")
        print("1. Add a New Task")
        print("2. View All Task")
        print("3. Remove a Task")
        print("4. Mark Complete")
        print("5. Exit")
        
        # input choice 
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addTask()
        elif choice == "2":
            viewTask()
        elif choice == "3":
            removeTask()
        elif choice == "4":
            MarkComplete()
        elif choice == "5":
            print("Existing the application....")
            exit()
        else:
            print("Invalid choice")
            
displayMenu()
            
        