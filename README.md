# Student Record Management System

## Overview
The Student Record Management System is a command-line Python application that allows an administrator to manage student academic records. It supports adding, viewing, searching, and deleting student data, and automatically saves all records to a local file so data persists between program runs. The system also generates an analytical report, including average marks, the topper, and a rank-based grading system.

This project was built as part of the Python Essentials course, applying core programming concepts including variables, loops, conditional statements, functions, dictionaries, lists, and file handling.

## Features
- **Add Student** — Enter a new student's roll number, name, and marks.
- **View All Students** — Display every currently stored student record.
- **Search Student** — Look up a student by roll number.
- **Delete Student** — Remove a student record by roll number.
- **View Report** — Displays:
  - Total number of students
  - Average marks
  - The topper (highest scorer)
  - Rank-based grading (S, A, B, C, D, E, F) for every student, based on relative performance
- **Persistent Storage** — All records are automatically saved to `students.txt` and reloaded the next time the program runs.

## Technologies / Tools Used
- **Language:** Python 3
- **Concepts used:** Functions, loops, conditionals, dictionaries, lists, string manipulation, file I/O
- **Editor:** Visual Studio Code
- **Version Control:** Git & GitHub

## Project Structure
student-record-management/
│
├── main.py               # Entry point: menu loop and program flow
├── student_manager.py    # Core operations: add, view, search, delete
├── file_handler.py       # Save/load student records to/from students.txt
├── reports.py            # Report generation and rank-based grading
├── students.txt          # Auto-generated data file (created on first run)
└── README.md

## How to Install & Run

**Prerequisites:** Python 3 installed on your system.

1. Clone this repository:........

2. Navigate into the project folder:cd student-record-management

3. Run the program:python3 main.py

4. Follow the on-screen menu to add, view, search, delete, or view the report.

## Testing Instructions

To verify the system works as expected:
1. Run the program and choose **Add Student** to add 4–5 records with varying marks.
2. Choose **View All Students** to confirm all records display correctly.
3. Choose **Search Student** with a valid and an invalid roll number to confirm both cases behave correctly.
4. Choose **Delete Student** to remove one record, then **View All Students** again to confirm it was removed.
5. Choose **View Report** to confirm the average, topper, and grade distribution are calculated correctly.
6. Exit the program and run it again to confirm previously entered data is still present (tests file persistence).

## Author
Tanmay Mishra
BTech CSE (Core), VIT Bhopal