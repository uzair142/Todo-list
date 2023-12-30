import sqlite3


def create_database():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()


    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL
        )
    ''')

    connection.commit()
    connection.close()


def add_task(task_name):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

    
    cursor.execute("INSERT INTO tasks (task_name) VALUES (?)", (task_name,))

    connection.commit()
    connection.close()


def view_tasks():
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

 
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()

    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        for task in tasks:
            print(f"ID: {task[0]}, Task: {task[1]}")

    connection.close()


def delete_task(task_id):
    connection = sqlite3.connect("tasks.db")
    cursor = connection.cursor()

   
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))

    connection.commit()
    connection.close()

def main():
    create_database()

    while True:
        print("\nTask Management System")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task by ID")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            add_task(task_name)
            print("Task added successfully!")
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = input("Enter the task ID to delete: ")
            delete_task(task_id)
            print("Task deleted successfully!")
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
