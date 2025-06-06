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

def latest_action_taken():
    global action_history_list
    action = action_history_list[-1]["action"]
    return action

def task_title(the_list, task_index):
    task_title = the_list[task_index][0][0]
    return task_title

def task_description(the_list, task_index):
    task_description = the_list[task_index][0][1]
    return task_description

def time_created(the_list, task_index):
    task_creation_time = the_list[task_index][2][0]
    return task_creation_time

def current_priority(the_list, task_index):
    task_priority = the_list[task_index][1]
    return task_priority

def welcome():
    print("\n\033[1mWhat would you like to do?\033[0m")
    print("Undo last action? (enter: 0)")
    print("Add Task? (enter: 1)")
    print("View Tasks details? (enter: 2)")
    print("Complete task? (enter: 3)")
    print("Remove Task? (enter: 4)")
    print("See completed Tasks? (enter: 5)")
    print("Change Priority of Task? (enter: 6)")
    print("Change Task description? (enter: 7)")
    print("Change Task Title? (enter: 8)")
    print("View Action History? (enter: 9)")
    print("Exit? (enter: 10) \n ")

# def choose_action():
#     print("\033[1mWhat Action Would You Like To Take?\033[0m")
#     print("Add Task?         (enter: 1)")   
#     print("Complete task?    (enter: 2)")
#     print("Remove Task?      (enter: 3)")
#     print("Undo last Action? (enter: 4)")
#     chosen_action = input("Enter Number Here: ")
#     if exit_to_menu(chosen_action):
#         return 
#     chosen_action = int(chosen_action)
#     if chosen_action == 1:
#         add_task(todo_list)
#     elif chosen_action == 2:
#         complete_task(todo_list, completed_list)
#     elif chosen_action == 3:
#         remove_task(todo_list, removed_tasks_list)
#     elif chosen_action == 4:
#         undo_last_action(todo_list, removed_tasks_list, completed_list)
#     else: 
#         print("Please choose valid number between 1 - 4")


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
            user_task_deadline_question = str(input("Would you like a deadline for the task (\"yes\" or \"no\")? (type \"exit\" to return to menu): ")).strip().lower()
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
    action_history_list.append({
        "action" : "Task Added",
        "index" : index,
        "task title" : user_task_title
        })
    # print(action_history_list) #testing to see if appended in correct format
    return alist                    


def view_current_base_tasks(alist):
    print("\nHere are the current outstanding tasks: ")
    if not alist:
        print("You have no tasks \n")
        return False
    for i, task in enumerate(alist):
            print("(Index: {}) Task: {:15} | Priority: {:6} | Deadline: {}".format(i, task_title(alist, i), current_priority(alist, i), task[2][1]))

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
        print("Task: \"{}\" has description: {} | Task was created on: {} \n".format(task_title(alist, index), task_description(alist, index), time_created(alist, index)))
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

def view_action_history():
    global action_history_list
    if not action_history_list:
        print("\nNothing in action history")
    print("Below are actions from earliest to latest:")
    for action in action_history_list:
        if action["action"] == "Task Added":
            print("Added Task : {}".format(action["task title"]))
        elif action["action"] == "Task Removed":
            print("Removed Task: \"{}\" from index \"{}\"".format(action["task title"], action["index"]))
        elif action["action"] == "Task Completed":
            print("Completed task \"{}\"".format(action["task title"]))
        elif action["action"] == "Priority Changed":
            print("Priority in Task \"{}\" changed from {} to {} ".format(action["task title"], action["old priority"], action["new priority"]))
        elif action["action"] == "Task Description Changed":
            print("Description for Task \"{}\" changed from {} to {}".format(action["task title"], action["old task description"], action["new task description"]))
        elif action["action"] == "Task Title Changed":
            print("Task Title at index \"{}\" changed from {} to {}".format(action["index"], action["old task title"], action["new task title"]))

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
    action_history_list.append({
        "action" : "Task Removed",
        "index" : index,
        "task title": removed_item[0][0],
        "full task info" : removed_item
        })
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
    action_history_list.append({
        "action" : "Task Completed", 
        "index" : index,
        "task info" : completed_item[0][0],
        "full task info" : completed_item
        })
    return alist

def change_task_description(alist):
    global action_history_list
    if view_current_base_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return   
    while True:
        task_index = input("Which Task description would you like to change? Choose a valid index: ").strip()     
        if exit_to_menu(task_index):
            return 
        index = index_validator(alist, task_index)
        if index is True:
            continue
        break 
    print("\nThe current description of this task is: \"{}\"".format(task_description(alist, index)))
    new_task_description = str(input("What would you like the new Description to be?: ")).strip()
    if exit_to_menu(new_task_description):
        return 
    old_task_description = task_description(alist, index)
    alist[index][0][1] = new_task_description
    action_history_list.append({
        "action" : "Task Description Changed", 
        "index" : index,
        "task title"  : task_title(alist, index), 
        "old task description" : old_task_description, 
        "new task description" : new_task_description
        })
    print("Description changed for task: {}   |   from {} to {}".format(task_title(alist, index), old_task_description, new_task_description))
    return alist

def change_task_title(alist):
    global action_history_list
    if view_current_base_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return   
    while True:
        task_index = input("Which Task Title would you like to change? Choose a valid index: ").strip()     
        if exit_to_menu(task_index):
            return 
        index = index_validator(alist, task_index)
        if index is True:
            continue
        break 
    new_task_title = str(input("What would you like the new Title to be?: ")).title()
    if exit_to_menu(new_task_title):
        return
    old_task_title = task_title(alist, index)
    alist[index][0][0] = new_task_title
    action_history_list.append({
        "action" : "Task Title Changed", 
        "index" : index, 
        "old task title" : old_task_title, 
        "new task title" : new_task_title
        })
    print("Title of Task at index {} changed from {} to {}".format(index, old_task_title, new_task_title))
        
def change_priority(alist):
    global action_history_list
    if view_current_base_tasks(alist) is False:
        print("No Tasks to complete, returning you to menu \n ......")
        return
    while True: 
        task_index = input("Which task would you like to change? Choose valid index: ").strip()
        if exit_to_menu(task_index): 
            return
        index = index_validator(todo_list, task_index)
        if index is True: 
            continue 
        while True: 
            new_priority = str(input("What priority level is this task (low/medium/high)? Type \"exit\" to return to menu:  ")).strip().lower()
            old_priority = current_priority(alist, index)
            if exit_to_menu(new_priority):
                return
            if priority_validator(new_priority, old_priority) is False:
                continue
            break
        break 
    task_title = task_title(alist, index)
    alist[index][1] = new_priority.upper()
    print("Priority of task \"{}\" has been changed from {} to {} \n".format(task_title, old_priority, new_priority.upper()))
    action_history_list.append({
        "action" : "Priority Changed", 
        "index" : index, 
        "task title" : task_title , 
        "old priority" : old_priority,
        "new priority" : new_priority
        })
    return alist 

def undo_last_action(alist, blist, clist): #todo_list, removed_tasks list, completed list
    global action_history_list
    if not action_history_list:
        print("No actions taken yet, nothing to undo")
        return 
    elif latest_action_taken() == "Task Added":
        print("Removing last task .....")
        action_history_list.pop()
        removed_item = alist.pop()
        blist.append(removed_item)
        action_history_list.clear()
        print("Removing the folowing Task: {}".format(removed_item[0][0]))
        return alist
    elif latest_action_taken() == "Task Removed":
        task_removed_dict = action_history_list[-1]
        removed_index = task_removed_dict["index"]
        removed_task = task_removed_dict["full task info"]
        alist.insert(removed_index, removed_task) #inserting task at correct index
        blist.pop()
        action_history_list.clear()
        print("\nTask: \"{}\" readded to todo_list at index: {}".format(removed_task[0][0], removed_index))
        return alist, blist
    elif latest_action_taken() == "Task Completed":
        task_completed_dict = action_history_list[-1]
        completed_index = task_completed_dict["index"]
        completed_task = task_completed_dict["full task info"]
        alist.insert(completed_index, completed_task)
        clist.pop()
        action_history_list.clear()
        print("\nTask: \"{}\" readded to todo_list at index: {}".format(completed_task[0][0], completed_index))
        return alist, clist
    elif latest_action_taken() == "Priority Changed":
        priority_changed_dict = action_history_list[-1]
        priority_index = priority_changed_dict["index"]
        task_title = priority_changed_dict["task title"]
        old_priority = priority_changed_dict["old priority"]
        new_priority = priority_changed_dict["new priority"]
        alist[priority_index][1] = old_priority.upper()
        action_history_list.clear()
        print("\nThe Priority of Task \"{}\" (at index: {}) has been changed back from {} to {}".format(task_title, priority_index, new_priority.upper(), old_priority))
        return alist
    elif latest_action_taken() == "Task Description Changed":
        description_changed_dict = action_history_list[-1]
        changed_desc_index = description_changed_dict["index"]
        task_title = description_changed_dict["task title"]
        old_task_desc = description_changed_dict["old task description"]
        new_task_desc = description_changed_dict["new task description"]
        alist[changed_desc_index][0][1] = old_task_desc
        action_history_list.clear()
        print("\nDescription for Task \"{}\" (at index: {}) has been changed back from {} to {}".format(task_title, changed_desc_index, new_task_desc, old_task_desc))
        return alist
    elif latest_action_taken() == "Task Title Changed":
        title_changed_dict = action_history_list[-1]
        changed_title_index = title_changed_dict["index"]
        old_task_title = title_changed_dict["old task title"]
        new_task_title = title_changed_dict["new task title"]
        alist[changed_title_index][0][0] = old_task_title
        action_history_list.clear()
        print("Title for task at index {} changed back from {} to {}".format(changed_title_index, new_task_title, old_task_title))
        return alist



todo_list = reading_file("currenttasks.csv")
completed_list = reading_file("completedtasks.csv")
removed_tasks_list = []
action_history_list = []
# print(completed_list) #testing current state of completed list
# print(todo_list) #testing current state of todo_list
while True: 
    welcome()
    try:
        choice = int(input("Enter number here:  "))
        if choice == 0:
            undo_last_action(todo_list, removed_tasks_list, completed_list)
        elif choice == 1:
            add_task(todo_list) 
        elif choice == 2:
            view_task_descriptions(todo_list)
        elif choice == 3:
            complete_task(todo_list, completed_list)
        elif choice == 4:
            remove_task(todo_list, removed_tasks_list)
        elif choice ==5:
            view_completed_tasks(completed_list)
        elif choice == 6:
            change_priority(todo_list)
        elif choice == 7:
            change_task_description(todo_list)
        elif choice == 8:
            change_task_title(todo_list)
        elif choice == 9:
            view_action_history()
        elif choice == 10:
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
