import os 

to_do_list = []

def add_task(task):
    to_do_list.append(task)
    print(f"Added : {task}") 

def remove_task(task_index):
    try:
        task = to_do_list.pop(task_index - 1)
        print(f"Task '{task}' removed!")
    except IndexError:
        print("Invalid task number!")

def save_tasks(filename="tasks.txt"):
    with open(filename, 'w') as file:
        for task in to_do_list:
            file.write(f"{task}\n")


def see_tasks():
    if not to_do_list:
        max_length = 20  # Default length for 'Nothing found!' message
        print_border(max_length)
        print("| Nothing found!          |")
        print_border(max_length)
    else:
        max_length = max(len(task) for task in to_do_list)  # Calculate the max length of tasks
        print_border(max_length)
        for index, task in enumerate(to_do_list, start=1):
            print(f"| {index}. {task:<{max_length}} |")  # Dynamically pad based on max length
        print_border(max_length)


def move_task():
    try: 
        original_index = int(input("Which one to move: "))
        task_to_move = to_do_list.pop(original_index - 1)
    except IndexError:
        print("Invalid task number! Unable to move.")
        return  # Exit the function if the index is invalid
    except ValueError:
        print("Please enter a valid number.")
        return
    
    try:
        new_index = int(input("Where to put it: ")) - 1 
        to_do_list.insert(new_index, task_to_move)
    except IndexError:
        print("Invalid new position! Task cannot be moved.")
    except ValueError:
        print("Please enter a valid number.")
def edit_task():
    original_index = int(input("Which one to edit: "))
    task_to_move = to_do_list.pop(original_index - 1)
    task = input("Edit: ")
    to_do_list.append(task)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def print_border(max_length):
    print('+' + '-' * (max_length + 5) + '+')

def main():
    filename="tasks.txt"
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                task = line.strip()
                to_do_list.append(task)
    while True:
        see_tasks()
        print("1 - Add, 2 - Move, 3 - Remove, 4 - Edit, 5 - Save")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == '2':
            move_task()
        elif choice == '3':
            task_index = int(input("Which one to remove : "))
            remove_task(task_index)
        elif choice == '4':
            edit_task()
        elif choice == '5':
            save_tasks()
            break
        else:
            print('Invalid number')
        clear_console()


if __name__ == "__main__":
    main()