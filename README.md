# Kode Camp's Week 4 Assignment Repository

## Task 1: Student Report Card App (with Version History)
### Goal: Build a terminal-based app to manage student scores and grades.

Features
- Student class: name, subjects, scores, average, grade
- Save/load data using JSON
- Use functions for operations (add, view, update)
- Use modules: os, json
- Use Git to track versions with commit messages like:
    * Add Student class and JSON save feature
    * Fix average score calculation

To run:

    cd task_1
    python main.py


## Task 2: Bookstore Inventory System (Using Git Branches)
### Goal: Build an app to manage books in a store.

Features:
- Book class: title, author, price, stock
- Use inventory.py for inventory logic
- Save inventory in books.json
- Use math module for rounding prices
- Use Git: Create and merge feature branches
    * git checkout -b feature-search
    * git merge feature-search

To run:

    cd task_2
    python main.py


## Task 4: File Organizer Tool (Real-Use Python Script)
### Goal: Automatically organize files into folders based on type.

Features:
- Use os and shutil modules
- Organize: .jpg/.png -> Images, .docx/.pdf -> Documents
- Get folder path from user input
- Handle errors using try-except
- Track changes using Git and meaningful commits

To run:

    cd task_4
    python main.py '<directory-path>'