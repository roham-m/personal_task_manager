import os
from dotenv import load_dotenv


load_dotenv()
admin_password = os.getenv("task_manager_ADMIN_PASSWORD")

open_admin = input("do u want to open admin mode?   yes/no:  ")

if open_admin.lower() == "yes":
    entered_password = input("enter admin password:  ")
    if entered_password == admin_password:
        print("admin! hi...")
    else:
        print("wrong password")

print("welcome to the personal_task_manager")

name = input("please enter your name: ")

tasks = []

while True:
    task = input(f"Hi {name}, please enter your task: ")

    difficulty = input("Is this task low, medium, or hard? ").lower()

    while difficulty not in ["low", "medium", "hard"]:
        difficulty = input("Please enter low, medium, or hard: ").lower()

    tasks.append(f"{task} ({difficulty})")

    add_tasks = input("Do you want to add another task? (y/n): ").lower()

    while add_tasks != "y" and add_tasks != "n":
        print("Invalid input!")
        add_tasks = input("Do you want to add another task? (y/n): ").lower()

    if add_tasks == "n":
        break

file = open("tasks.txt", "a")

file.write(f"{name} tasks:\n")

for task in tasks:
    file.write(task + "\n")

file.write("\n")
file.close()

print(f"\n{name} tasks:")

for task in tasks:
    print(task)