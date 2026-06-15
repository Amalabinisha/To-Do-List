# To-Do List (CLI)

1. PROJECT OVERVIEW
TodoManager is a structured task management system built in Python using built-in modules. It demonstrates the fundamental pipeline of CRUD operations with data persistence using JSON. The system uses priority levels + status tracking + filtering for enhanced productivity.

This project satisfies the "TASK 3 SPECIFICATION: TO-DO LIST (CLI)" requirements for a menu-driven task manager.

2. FEATURES & REQUIREMENTS MET

ADD TASKS: Captures title, description, priority, and due date
DELETE TASKS: Removes tasks by ID with confirmation prompt
VIEW TASKS: Displays formatted table with color-coded status and priority
MENU-DRIVEN CLI: 6-option menu loop for all operations
ENHANCEMENT: Mark complete + filter by status/priority + auto-save + task stats

3. HOW TO RUN

Prerequisites:
- Python 3.9+ installed

Steps:
1. Open terminal and run: python todo_manager.py
2. Select options 1-6 from the menu
3. Data auto-saves to todo_list.json after every operation
4. Use option 2 to view all tasks with stats

4. PROJECT STRUCTURE

todo_list_cli/
├── todo_manager.py - Main CRUD + menu logic
├── todo_list.json - Auto-generated data file
└── README.md - This file

5. HOW IT WORKS - THE IPO MODEL
1. Input: `input()` captures task details and menu choices
2. Process: Tasks stored as dictionaries in list. `json.dump()` saves to file. Filters use list comprehension
3. Output: Color-coded table displays tasks. Stats show total/done/pending count

6. KEY CONCEPTS DEMONSTRATED
1. CRUD Operations: Create, Read, Update, Delete implemented for tasks
2. Data Persistence: JSON file ensures tasks survive program restart
3. Data Validation: Checks for empty title + invalid ID entry
4. User Experience: ANSI colors + priority levels + status tracking for clarity
5. Data Management: Auto ID re-numbering + timestamp tracking
6. Filtering Logic: List comprehension filters tasks by status or priority

