import csv
import ast
from datetime import datetime


def reading_file(filename):
    try:
        with open(filename, "r") as filelist:
            alist = []
            read = csv.reader(filelist)
            for row in read:
                task = ast.literal_eval(row[0])
                alist.append(task)
            return alist
    except FileNotFoundError:
        alist = []
        return alist
    
def writing_file(filename, alist):
    with open(filename, "w") as filelist:
        writer = csv.writer(filelist)
        for task in alist:
            writer.writerow([str(task)])

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
    
def check_priority_is_valid(input_priority):
    if input_priority not in ["high", "medium", "low"]:  
        print("Please enter one of the following priorities: \"low\", \"medium\", or \"high\" or \"exit\" to exit to main menu:  ")  
        return True

def check_same_priority(input_priority, existing_priority):
    if input_priority.upper() == existing_priority:
        return True

def index_validator(alist, input_index):
    if check_index_is_integar(input_index):
        print("Please enter a integar or \"exit\" \n")
        return True
    index = int(input_index)
    if check_index_in_range(alist, index):
        print("Please input valid index in between 0 and {} :".format(len(alist)-1))
        return True 
    return index

def priority_validator(priority, existing_priority):
    if check_priority_is_valid(priority):
        return False
    if check_same_priority(priority, existing_priority):
        print("This is the same priority as before .. ")
        return False


def welcome():
    print("\n\033[1mWhat would you like to do?\033[0m")
    print("Undo last action? (enter: 0)")
    print("Add Task? (enter: 1)")
    print("View Tasks details? (enter: 2)")
    print("Complete task? (enter: 3)")
    print("Remove Task? (enter: 4)")
    print("See completed Tasks? (enter: 5)")
    print("Change Priority of Task? (enter: 6)")
    print("Exit? (enter: 7) \n ")


def add_task(alist):
    global action_history_list
    user_task_title = str(input("What is the title of your task (type \"exit\" to return to menu): ")).strip().title()
    if exit_to_menu(user_task_title):
        return
    user_task_description = str(input("Please enter task description (type \"exit\" to return to menu): ")).strip()
    if exit_to_menu(user_task_description):
        return 
    while True:
        priority = str(input("What priority level is this task (low/medium/high)? Type \"exit\" to return to menu:  ")).strip().lower()
        if exit_to_menu(priority):
            return
        if check_priority_is_valid(priority):
            continue
        while True: 
            user_task_deadline_question = str(input("Would you like a deadline for the task? (type \"exit\" to return to menu): ")).strip().lower()
            if exit_to_menu(user_task_deadline_question):
                return 
            if user_task_deadline_question not in ["yes", "no"]:
                print("Please enter \"yes\" or \"no\"!")
                continue
            if user_task_deadline_question == "yes":
                user_task_deadline = str(input("What deadline would you like to set?: "))
                if exit_to_menu(user_task_deadline):
                    return 
            elif user_task_deadline_question == "no":
                user_task_deadline = "No Deadline"
            break
        break
    now = str(datetime.now())
    new_task = [[user_task_title, user_task_description], priority.upper(), [now, user_task_deadline]]
    alist.append(new_task)
    index = len(alist) - 1
    print("\nYour new task is located at the following index: {}  \n".format(index))
    action_history_list.append(["Task Added", new_task])
    # print(action_history_list) #testing to see if appended in correct format
    return alist                    


def view_current_base_tasks(alist):
    print("\nHere are the current outstanding tasks: ")
    if not alist:
        print("You have no tasks \n")
        return False
    for i, task in enumerate(alist):
            print("(Index: {}) Task: {:15} | Priority: {:6} | Deadline: {}".format(i, task[0][0], task[1], task[2][1]))

def view_task_descriptions(alist):
    if view_current_base_tasks(alist) is False:
        print("No Tasks ...")
        return
    while True:
        user_task_description_index = input("Which Task details would you like to see? Please choose a valid index: ").strip()
        if exit_to_menu(user_task_description_index):
            return
        index = index_validator(todo_list, user_task_description_index)
        if index is True:
            continue
        print("Task: \"{}\" has description: {} | Task was created on: {} \n".format(alist[index][0][0], alist[index][0][1], alist[index][2][0]))
        while True:
            user_go_again = str(input("Would you like to view another Task description? (Answer \"yes\" or \"no\"): ")).strip().lower()
            if exit_to_menu(user_go_again):
                return
            if user_go_again not in ["yes", "no"]:
                print("Please choose answer \"yes\" or \"no\"!\n")
                continue
            break
        if user_go_again == "yes":
            continue
        elif user_go_again == "no":
            return
        break 

def view_completed_tasks(alist):
    print("Here are all completed tasks: ")
    if not alist:
        print("You're useless and haven't completed anytasks \n")
        return False
    for task in alist:
            print("Task completed: {}".format(task[0][0]))

def remove_task(alist, blist):
    global action_history_list
    if view_current_base_tasks(alist) is False:
        print("No Tasks to return, returning you to menu \n ......")
        return
    while True:
        removed_index = input("Which task would you like to remove? Please enter index number (type \"exit\" to return to menu): ").strip()
        if exit_to_menu(removed_index):
            return
        index = index_validator(todo_list, removed_index)
        if index is True:
            continue
        break 
    removed_item = alist.pop(index)
    blist.append(removed_item)
    print("\nTask: \"{}\" has been removed from current tasks. \n".format(removed_item[0][0]))
    view_current_base_tasks(alist)
    action_history_list.append(["Task Removed", index, removed_item])
    return alist

            
def complete_task(alist, clist):
    global action_history_list
    if view_current_base_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return
    while True:
        completed_index = input("Which task would you like to complete? Please enter index number (type \"exit\" to return to menu): ")
        if exit_to_menu(completed_index):
            return
        index = index_validator(todo_list, completed_index)
        if index is True:
            continue
        break 
    completed_item = alist.pop(index)
    clist.append(completed_item)
    print("\n Task \"{}\" has been removed from current tasks. \n".format(completed_item[0][0]))
    view_current_base_tasks(alist)
    action_history_list.append(["Task Completed", index, completed_item])
    return alist


def change_priority(alist):
    global action_history_list
    if view_current_base_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return
    while True: 
        task_index = input("Which task would you like to change. Please choose valid index: ").strip()
        if exit_to_menu(task_index): 
            return
        index = index_validator(todo_list, task_index)
        if index is True: 
            continue 
        while True: 
            new_priority = str(input("What priority level is this task (low/medium/high)? Type \"exit\" to return to menu:  ")).strip().lower()
            old_priority = alist[index][1]
            if exit_to_menu(new_priority):
                return
            if priority_validator(new_priority, old_priority) is False:
                continue
            break
        break 
    only_task = alist[index][0]
    alist[index][1] = new_priority.upper()
    print("Priority of task \"{}\" has been changed from {} to {} \n".format(only_task[0], old_priority, new_priority))
    action_history_list.append(["Priority Changed", index, only_task , old_priority, new_priority])
    return alist 

def undo_last_action(alist, blist, clist): #todo_list, removed_tasks list, completed list
    global action_history_list
    if not action_history_list:
        print("No actions taken yet, nothing to undo")
        return 
    elif action_history_list[-1][0] == "Task Added":
        print("Removing last task .....")
        action_history_list.pop()
        removed_item = alist.pop()
        blist.append(removed_item)
        action_history_list.clear()
        print("Removing the folowing Task: {}".format(removed_item[0][0]))
        return alist
    elif action_history_list[-1][0] == "Task Removed":
        removed_index = action_history_list[-1][1]
        removed_task = action_history_list[-1][2]
        alist.insert(removed_index, removed_task) #inserting task at correct index
        blist.pop()
        action_history_list.clear()
        print("\nTask: \"{}\" readded to todo_list at index: {}".format(removed_task[0][0], removed_index))
        return alist, blist
    elif action_history_list[-1][0] == "Task Completed":
        completed_index = action_history_list[-1][1]
        completed_task = action_history_list[-1][2]
        alist.insert(completed_index, completed_task)
        clist.pop()
        action_history_list.clear()
        print("\nTask: \"{}\" readded to todo_list at index: {}".format(completed_task[0][0], completed_index))
        return alist, clist
    elif action_history_list[-1][0] == "Priority Changed":
        priority_index = action_history_list[-1][1]
        task_info = action_history_list[-1][2]
        old_priority = action_history_list[-1][3]
        new_priority = action_history_list[-1][4]
        alist[priority_index][1] = old_priority.upper()
        action_history_list.clear()
        print("\nThe Priority of Task \"{}\" (at index: {}) has been changed from {} to {}".format(task_info[0], priority_index, new_priority.upper(), old_priority))
        return alist


todo_list = reading_file("currenttasks.csv")
completed_list = reading_file("completedtasks.csv")
removed_tasks = []
action_history_list = []
# print(completed_list) #testing current state of completed list
# print(todo_list) #testing current state of todo_list
while True: 
    welcome()
    try:
        choice = int(input("Enter number here:  "))
        if choice == 0:
            undo_last_action(todo_list, removed_tasks, completed_list)
        elif choice == 1:
            add_task(todo_list) 
        elif choice == 2:
            view_task_descriptions(todo_list)
        elif choice == 3:
            complete_task(todo_list, completed_list)
        elif choice == 4:
            remove_task(todo_list, removed_tasks)
        elif choice ==5:
            view_completed_tasks(completed_list)
        elif choice == 6:
            change_priority(todo_list)
        elif choice == 7:
            print("Shutting down todo-list app \n ....")
            writing_file("currenttasks.csv", todo_list)
            writing_file("completedtasks.csv", completed_list)
            # print(todo_list) #used for testing output to file
            break
        else:
            print("Please choose a valid number (1-7) \n")
    except ValueError:
        print("Must be an integar between 1-7, please try again \n ")
    except IndexError:
        print("Must be between 1-7: \n ")
