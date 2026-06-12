def get_students():
    students = []
    student_number = int(input("enter student number:"))

    for number in range(1, student_number + 1):
        name = input(f"student {number} name: ").strip()
        score = float(input(f"student {number} score: "))
        attendance = float(input(f"student {number} attendance: "))

        student = {
            "name": name,
            "score": score,
            "attendance": attendance
        }
        students.append(student)
    return students

def save_infor(students):
    with open ("students.csv", "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"{student['name']}, {student['score']}, {student['attendance']}\n")

def read_infor():
    students = []
    with open ("students.csv", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            part = line.split(",")

            student = {
                "name": part[0],
                "score": part[1],
                "attendance": part[2]
            }
            students.append(student)
    return students

def provide_students(students):
    for student in students:
        print("---student---")
        print(student["name"])
        print(student["score"])
        print(student["attendance"])


students = get_students()
save_infor(students)

print("students are saved to student.csv")

loaded_students = read_infor()
provide_students(loaded_students)
