print("welcome to the personal_task_manager")

name = input("pleaze enter your name: ")

tasks = input(f"Hi {name}, pleaze enter the new tasks:  ")

print_or_no = input("do you want to see yor tasks: (y/n)")

if print_or_no == "y":
    print(f"These are all your tasks: \n task1: {tasks}")
else:
    print("ok")