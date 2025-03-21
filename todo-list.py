
def reading_file(filename):
    try:
        with open(filename, "r") as filelist:
            alist = []
            for line in filelist.readlines():
                alist.append(line.strip())
            return alist
    except FileNotFoundError:
        alist = []
        return alist
    

def writing_file(filename, alist):
    with open(filename, "w") as filelist:
        for task in alist:
            filelist.write("{}\n".format(task))




def welcome():
    print("\nWhat would you like to do?")
    print("Add Task? (enter: 1)")
    print("View Tasks? (enter: 2)")
    print("Complete task? (enter: 3)")
    print("Remove Task? (enter: 4)")
    print("See completed Tasks? (enter: 5)")
    print("Exit? (enter: 6) \n ")

def add_task(alist):
    new_task = str(input("What task would you like to add (type \"exit\" to return to menu): "))
    if new_task == "exit":
        return
    else:
        alist.append(new_task)
        index = len(alist) - 1
        print("The task is located at the following index: {}  \n".format(index))
        return alist

def view_current_tasks(alist):
    print("Here are the current outstanding tasks: ")
    if not alist:
        print("You have no tasks \n")
        return False
    for i, task in enumerate(alist):
            print("Index: {}. Task: {}".format(i, task))

def view_completed_tasks(alist):
    print("Here are all completed tasks: ")
    if not alist:
        print("You're useless and haven't completed anytasks \n")
        return False
    for task in alist:
            print("Task completed: {}".format(task))

def remove_task(alist):
    if view_current_tasks(alist) is False:
        print("No Tasks to return, returning you to menu \n ......")
        return
    while True:
        try:
            removed = input("Which task would you like to remove? Please enter index number (type \"exit\" to return to menu): ")
            if removed == "exit":
                return
            else:
                removed = int(removed)
                alist.pop(removed)
                print("\n Task removed from current tasks.")
                view_current_tasks(alist)
                return alist
        except ValueError:
            print("Please input a valid integar representing a Task index or exit \n")
        except IndexError:
            print("Please input a valid integar representing a Task Index or exit \n")

def complete_task(alist, clist):
    if view_current_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return
    while True:
        try:
            removed = input("Which task would you like to complete? Please enter index number (type \"exit\" to return to menu): ")
            if removed == "exit":
                return
            else:
                removed = int(removed)
                removed_item = alist.pop(removed)
                clist.append(removed_item)
                print("\n Task removed from current tasks.")
                view_current_tasks(alist)
                return alist
        except ValueError:
            print("Please input a valid integar representing a Task index or exit \n")
        except IndexError:
            print("Please input a valid integar representing a Task Index or exit \n")       


todo_list = reading_file("currenttasks.txt")
completed_list = reading_file("completedtasks.txt")
# print(completed_list) #testing current state of completed list
# print(todo_list) #testing current state of todo_list
while True: 
    welcome()
    try:
        choice = int(input("Enter number here: "))
        if choice == 1:
            add_task(todo_list) 
        elif choice == 2:
            view_current_tasks(todo_list)
        elif choice == 3:
            complete_task(todo_list, completed_list)
        elif choice == 4:
            remove_task(todo_list)
        elif choice ==5:
            view_completed_tasks(completed_list)
        elif choice == 6:
            print("Shutting down todo-list app \n ....")
            writing_file("currenttasks.txt", todo_list)
            writing_file("completedtasks.txt", completed_list)
            # print(todo_list) #used for testing out[ut to file
            break
        else:
            print("Please choose a valid number (1-4) \n")
    except ValueError:
        print("Must be an integar between 1-4, please try again \n ")
    except IndexError:
        print("Must be between 1-4: \n ")
