# todo.py
def display_menu():
    print("1. Enter your Task here!")
    print("2. View all the tasks here.")
    print("3. Exit")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def view_tasks(tasks):
    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            break
        else:
            print("Wrong choice. Please try again.")

if __name__ == "__main__":
    main()