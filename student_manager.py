from reports import calculate_grade
def add_student(students):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")

    student = {"roll": roll, "name": name, "marks": marks}
    students.append(student)

    print("Student added successfully!")

def view_students(students):
    if len(students) == 0:
        print("No records found.")
        return

    print("\n--- All Student Records ---")
    for student in students:
        grade = calculate_grade(student["marks"])
        print("Roll:", student["roll"], "| Name:", student["name"], "| Marks:", student["marks"], "| Grade:", grade)



def search_student(students):
    roll_to_find = input("Enter roll number to search: ")
    found = False

    for student in students:
        if student["roll"] == roll_to_find:
            print("Student found!")
            print("Roll:", student["roll"], "| Name:", student["name"], "| Marks:", student["marks"])
            found = True

    if not found:
        print("No student found with that roll number.")


def delete_student(students):
    roll_to_delete = input("Enter roll number to delete: ")
    found = False

    for student in students:
        if student["roll"] == roll_to_delete:
            students.remove(student)
            found = True
            print("Student deleted successfully!")
            break

    if not found:
        print("No student found with that roll number.")