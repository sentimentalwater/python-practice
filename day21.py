def store_students():
    students = []
    total_student = int(input("enter student number: "))

    for number in range(1, total_student + 1):
        name = input(f"enter student {number} name: ").strip()
        score = float(input(f"enter student {number} score: "))
        attendance = float(input(f"enter student {number} attendance: "))

        student = {
            "name": name,
            "score": score,
            "attendance": attendance
        }
        students.append(student)

    return students

def save_infor(students):
    with open ("students.txt", "w", encoding="utf-8") as file:
        for student in students:
            file.write("---student---\n")
            file.write(f"name: {student['name']} \n")
            file.write(f"name: {student['score']} \n")
            file.write(f"attendance: {student['attendance']} \n")

students = store_students()
save_infor(students)

print("student are saved to students.txt")