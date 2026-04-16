To-Do List Manager 📝
A simple command-line To-Do List Manager built in Python. This was a personal project I worked on during my free time — fully written in Python, my strongest language, with the code manually written by me.


About
This is a lightweight task manager that runs in the terminal. It lets you add, view, mark, and delete tasks — all stored locally in a text file. No libraries, no frameworks, just pure Python.


Features
View all your tasks
Add new tasks
Mark tasks as done
Delete tasks
Data is saved locally so tasks persist between sessions


Project Structure
To-do-List---Mini-Project/

│

├── Menu.py        # Main file — runs the app and displays the menu

├── Tasksfunc.py   # Contains all task functions (view, add, mark, delete)

├── .gitignore     # Excludes Tasks.txt from being tracked

└── README.md      # You're reading this!


How to Run
Make sure Python is installed on your system.

python Menu.py

Once running, you'll see a menu like this:

To-Do-List Manager

1. View Tasks

2. Add Tasks

3. Mark Task As Done

4. Delete Task

5. Exit

A Tasks.txt file will be created automatically the first time you add a task. This file is excluded from the repo via .gitignore.


Tech Stack
Language: Python 🐍
Storage: Local text file (Tasks.txt)
No external libraries used
