# =====importing libraries===========
'''This is the section where you will import libraries'''

from datetime import date
# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''
# Load user data from user.txt into a dictionary
users = {}

with open("user.txt", "r") as file:
    for line in file:
        username, password = line.strip().split(", ")
        users[username] = password


def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

def register_user():
    if current_user != "admin":
        print("You don't have access to register users.")
        return

    new_username = input("Enter a new username: ")
    if new_username in users:
        print("Username already exists.")
        return

    new_password = input("Enter a new password: ")
    confirm_password = input("Confirm the password: ")
    if new_password != confirm_password:
        print("Passwords do not match.")
        return

    hashed_password = new_password
    users[new_username] = hashed_password

    with open("user.txt", "a") as file:
        file.write(f"\n{new_username}, {hashed_password}")
    print("User successfully registered.")


current_user = None

while True:
    if current_user:
        menu = input("Select one of the following options:\n"
                     "a - Add task\n"
                     "va - View all tasks\n"
                     "vm - View my tasks\n"
                     "stats - Show statistics\n"
                     "e - Exit\n"
                     ": ").lower()
    else:
        menu = input("Select one of the following options:\n"
                     "r - Register a user\n"
                     "a - Add task\n"
                     "va - View all tasks\n"
                     "vm - View my tasks\n"
                     "e - Exit\n"
                     ": ").lower()

    if menu == 'r':
        register_user()
    elif menu == 'a':
        if current_user:
            user_name = current_user
            task_title = input("Enter the title of the task: ")
            task_description = input("Enter the description of the task: ")
            due_date = input("Enter the due date of the task (YYYY-MM-DD): ")
            current_date = date.today().strftime("%Y-%m-%d")
            status = input("Is the task completed? (Yes/No): ").lower()

            with open("tasks.txt", "a") as file:
                file.write(f"\n{user_name}, {task_title}, {task_description}, {due_date}, {current_date}, {status}")
            print("Task added successfully.")
        else:
            print("Please log in to add a task.")
    elif menu == 'va':
        with open("tasks.txt", "r") as file:
            for line in file:
                task_info = line.strip().split(", ")
                print(f"Task: {task_info[1]}\n"
                      f"Assigned to: {task_info[0]}\n"
                      f"Date Assigned: {task_info[4]}\n"
                      f"Due date: {task_info[3]}\n"
                      f"Task complete?: {task_info[5]}\n")
    elif menu == 'vm':
        if current_user:
            user_tasks = []
            with open("tasks.txt", "r") as file:
                for line in file:
                    task_info = line.strip().split(", ")
                    if task_info[0] == current_user:
                        user_tasks.append(task_info)

            if user_tasks:
                for task_info in user_tasks:
                    print(f"Task: {task_info[1]}\n"
                          f"Assigned to: {task_info[0]}\n"
                          f"Date Assigned: {task_info[4]}\n"
                          f"Due date: {task_info[3]}\n"
                          f"Task complete?: {task_info[5]}\n")
            else:
                print("You have no tasks.")
        else:
            print("Please log in to view your tasks.")
    elif menu == 'stats':
        num_users = len(users)
        num_tasks = 0
        with open("tasks.txt", "r") as file:
            num_tasks = sum(1 for line in file)

        print(f"Number of users registered: {num_users}")
        print(f"Number of tasks: {num_tasks}\n")
    elif menu == 'e':
        print('Goodbye!')
        break
    else:
        print("Invalid input. Please try again.")

    if not current_user:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if login(username, password):
            current_user = username
        else:
            print("Invalid username or password. Please try again.")