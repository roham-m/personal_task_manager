print("welcome to the personal_task_manager")

name = input("please enter your name: ")

tasks = []

while True:
    task = input(f"Hi {name}, please enter your task: ")
    tasks.append(task)

    add_tasks = input("Do you want to add another task? (y/n) ")

    if add_tasks == "n":
        break

print(f"\nThese are all your tasks: \n {tasks}")

