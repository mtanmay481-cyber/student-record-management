import os


def save_students(students):
    file = open("students.txt", "w")

    for student in students:
        line = student["roll"] + "," + student["name"] + "," + student["marks"] + "\n"
        file.write(line)

    file.close()


def load_students():
    students = []

    if os.path.exists("students.txt") == False:
        return students

    file = open("students.txt", "r")

    for line in file:
        line = line.strip()
        parts = line.split(",")
        student = {"roll": parts[0], "name": parts[1], "marks": parts[2]}
        students.append(student)

    file.close()
    return students