from file_handler import save_students, load_students
from student_manager import add_student, view_students, search_student, delete_student
from reports import show_report


def main():
    students = load_students()

    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. View Report")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
            save_students(students)
        elif choice == "5":
            show_report(students)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


main()