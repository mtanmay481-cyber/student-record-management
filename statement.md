# Project Statement

## Problem Statement
Instructors and small institutions often need a lightweight way to record and track basic student
performance data without relying on complex, dependency-heavy database systems or external software.
Paper records are error-prone and hard to search, and spreadsheet tools require extra software.
This project provides a simple, dependency-free, terminal-based application for managing student
records using only Python's built-in features, with data persisted between sessions in a text file.

## Scope of the Project
**In scope**
- Adding, viewing, searching, and deleting student records (roll number, name, marks)
- Automatic saving to and loading from `students.txt`
- A summary report: total students, average marks, topper, and rank-based grades

**Out of scope (future enhancements)**
- Input validation for non-numeric marks and duplicate roll numbers
- Subject-wise marks
- Database storage (SQLite) and GUI / web front end
- Report export to CSV or PDF

## Target Users
- Instructors or administrators of small classes who need quick record keeping
- Beginner Python learners who want to study a small, modular, file-based application

## High-Level Features
1. **Student Management** – add, view, search, and delete records
2. **File Persistence** – records are saved automatically and reloaded on the next run
3. **Reports & Analytics** – count, average, topper, and rank-based grading (S, A, B, C, D, E, F)
4. **Menu-driven interface** – numbered terminal menu that loops until the user exits
