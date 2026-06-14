from student_utils import get_number, get_students, print_students, print_summary
from file_utils import save_students, read_students

while True:
    print("----- Student System -----")
    print("1. Add student")
    print("2. View students")
    print("3. Show summary")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        student = get_students()
        get_students(student)
        print("Student saved.")

    elif choice == "2":
        students = read_students()
        print_students(students)

    elif choice == "3":
        students = read_students()
        print_summary(students)

    elif choice == "4":
        print("Exit.")
        break

    else:
        print("Invalid choice.")