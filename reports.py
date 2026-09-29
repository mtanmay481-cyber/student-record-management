
def show_report(students):
    if len(students) == 0:
        print("No records found.")
        return

    total_students = len(students)
    total_marks = 0

    for student in students:
        total_marks = total_marks + int(student["marks"])

    average_marks = total_marks / total_students

    topper = students[0]
    for student in students:
        if int(student["marks"]) > int(topper["marks"]):
            topper = student

    print("\n--- Report ---")
    print("Total students:", total_students)
    print("Average marks:", average_marks)
    print("Topper: Roll", topper["roll"], "| Name:", topper["name"], "| Marks:", topper["marks"])
    print("DEBUG: reached this point")

    grade_map = get_relative_grade_map(students)

    print("\n--- Relative Grades (Rank-Based) ---")
    for student in students:
        marks = int(student["marks"])
        grade = grade_map[marks]
        print("Roll:", student["roll"], "| Name:", student["name"], "| Marks:", student["marks"], "| Grade:", grade)


def get_relative_grade_map(students):
    unique_marks = []

    for student in students:
        marks = int(student["marks"])
        if marks not in unique_marks:
            unique_marks.append(marks)

    unique_marks.sort(reverse=True)

    grade_labels = ["S", "A", "B", "C", "D", "E", "F"]
    grade_map = {}

    for i in range(len(unique_marks)):
        if i < len(grade_labels):
            grade_map[unique_marks[i]] = grade_labels[i]
        else:
            grade_map[unique_marks[i]] = grade_labels[-1]

    return grade_map
def calculate_grade(marks):
    marks = int(marks)

    if marks >= 90:
        return "S"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"