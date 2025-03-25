import csv
counter = 0

class PriorityError(Exception):
    pass

def reading_file(filename):
    try:
        with open(filename, "r") as filelist:
            alist = []
            read = csv.reader(filelist)
            for line in read:
                alist.append(line)
            return alist
    except FileNotFoundError:
        alist = []
        return alist
    
def writing_file(filename, alist):
    with open(filename, "w") as filelist:
        writer = csv.writer(filelist)
        writer.writerows(alist)

def exit_to_menu(user_input):
    if user_input.lower() == "exit":
        print("Exiting to Main Menu \n ......")
        return True

def check_index_is_integar(input_index):
    if not input_index.isdigit():
        return True

def check_index_in_range(alist, input_index):
    input_index = int(input_index)
    if input_index not in range(0, len(alist)):
        return True

def index_validator(alist, input_index):
    if check_index_is_integar(input_index):
        print("Please enter a integar or \"exit\" \n")
        return False
    index = int(input_index)
    if check_index_in_range(alist, index):
        print("Please input valid index in between 0 and {} :".format(len(alist)-1))
        return False 
    return index

def priority_validator(priority, existing_priority = None):
    if priority not in ["high", "medium", "low"]:
        print("Please enter one of the following priorities: \"low\", \"medium\", or \"high\" or \"exit\" to exit to main menu:  ")
        return False
    if existing_priority is not None:
        if priority.upper() == existing_priority[13:]:
            print("This is the same priority as before .. ")
            return False


def welcome():
    print("\nWhat would you like to do?")
    print("Undo last action? (enter: 0)")
    print("Add Task? (enter: 1)")
    print("View Tasks? (enter: 2)")
    print("Complete task? (enter: 3)")
    print("Remove Task? (enter: 4)")
    print("See completed Tasks? (enter: 5)")
    print("Change Priority of Task? (enter: 6)")
    print("Exit? (enter: 7) \n ")


def add_task(alist):
    global counter
    while True:
        user_task = str(input("What task would you like to add (type \"exit\" to return to menu): "))
        if exit_to_menu(user_task):
            return
        priority = str(input("What priority level is this task (low/medium/high)? Type \"exit\" to return to menu:  ")).lower()
        if exit_to_menu(priority):
            return
        if priority_validator(priority) is False:
            continue
        break 
    new_task = [user_task, "priority is: {}".format(priority.upper())]
    alist.append(new_task)
    index = len(alist) - 1
    print("The task is located at the following index: {}  \n".format(index))
    counter = 1
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

def remove_task(alist, blist):
    global counter
    if view_current_tasks(alist) is False:
        print("No Tasks to return, returning you to menu \n ......")
        return
    while True:
        try:
            removed = input("Which task would you like to remove? Please enter index number (type \"exit\" to return to menu): ")
            if exit_to_menu(removed):
                return
            else:
                removed = int(removed)
                removed_item = alist.pop(removed)
                blist.append(removed_item)
                print(blist)
                print("\n Task removed from current tasks.")
                view_current_tasks(alist)
                counter = 2
                return alist
        except ValueError:
            print("Please input a valid integar representing a Task index or exit \n")
        except IndexError:
            print("Please input a valid integar representing a Task Index or exit \n")

def complete_task(alist, clist):
    global counter
    if view_current_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return
    while True:
        try:
            removed = input("Which task would you like to complete? Please enter index number (type \"exit\" to return to menu): ")
            if exit_to_menu(removed):
                return
            else:
                completed = int(removed)
                completed_item = alist.pop(completed)
                clist.append(completed_item)
                print("\n Task removed from current tasks.")
                view_current_tasks(alist)
                counter = 3
                return alist
        except ValueError:
            print("Please input a valid integar representing a Task index or exit \n")
        except IndexError:
            print("Please input a valid integar representing a Task Index or \"exit\" \n")      

def change_priority(alist):
    global counter
    if view_current_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return
    while True: 
        task_index = input("Which task would you like to change. Please choose valid index: ")
        if exit_to_menu(task_index): #checks if input was "exit"
            return
        index = index_validator(todo_list, task_index)
        if index is False: 
            continue 
        while True: 
            priority = str(input("What priority level is this task (low/medium/high)? Type \"exit\" to return to menu:  ")).lower()
            current_priority = alist[index][1]
            if exit_to_menu(priority):
                return
            if priority_validator(priority, current_priority) is False:
                continue
            break
        break 
    alist[index][1] = "priority is: {}".format(priority.upper())
    counter = 4
    return alist 

def undo_last_action(alist, blist, clist): #todo_list, removed_tasks list, completed list
    global counter
    if counter == 0:
        print("No actions taken yet, nothing to undo")
        return 
    elif counter == 1:
        print("Removing last task .....")
        removed_item = alist.pop()
        blist.append(removed_item)
        return alist, blist
    elif counter == 2:
        print("Re-adding last removed task ....")
        adding_item = blist.pop()
        alist.append(adding_item)
        return alist, blist
    elif counter == 3:
        print("Fetching completed task .....")
        completed = clist.pop()
        alist.append(completed)
    counter = 0

todo_list = reading_file("currenttasks.csv")
completed_list = reading_file("completedtasks.csv")
removed_tasks = []
# print(completed_list) #testing current state of completed list
# print(todo_list) #testing current state of todo_list
while True: 
    welcome()
    try:
        choice = int(input("Enter number here: "))
        if choice == 0:
            undo_last_action(todo_list, removed_tasks, completed_list)
        elif choice == 1:
            add_task(todo_list) 
            # print(counter) #testing counter
        elif choice == 2:
            view_current_tasks(todo_list)
        elif choice == 3:
            complete_task(todo_list, completed_list)
            # print(counter) #testing counter
        elif choice == 4:
            remove_task(todo_list, removed_tasks)
            # print(counter) #testing counter
        elif choice ==5:
            view_completed_tasks(completed_list)
        elif choice == 6:
            change_priority(todo_list)
        elif choice == 7:
            print("Shutting down todo-list app \n ....")
            writing_file("currenttasks.csv", todo_list)
            writing_file("completedtasks.csv", completed_list)
            # print(todo_list) #used for testing out[ut to file
            break
        else:
            print("Please choose a valid number (1-7) \n")
    except ValueError:
        print("Must be an integar between 1-7, please try again \n ")
    except IndexError:
        print("Must be between 1-7: \n ")
