students = []

total_students = int(input("enter students number: "))

for number in range(1, total_students + 1):
    name = input(f"enter student {number} name: ").strip()
    score = float(input(f"enter student {number} score: "))
    attendance = float(input(f"enter student {number} attendance: "))

    student = {
        "name": name,
        "score": score,
        "attendance": attendance
    }

    students.append(student)

print("---students---")

for student in students:
    print("student name: ", student["name"])
    print("student score: ", student["score"])
    print("student attendance: ", student["attendance"])

    if student["score"] >= 60 and student["attendance"] >= 80:
        print("pass")
    else:
        print("fail")

print("------------")