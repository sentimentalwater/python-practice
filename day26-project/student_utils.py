def get_students():
    students = []
    total_number = int(input("enter student number: "))
    for number in range(1, total_number + 1):
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

def print_students(students):
    for student in students:
        print("-student--")
        print("name:", student["name"])
        print("score:", student["score"])
        print("attendance:", student["attendance"])

def get_average(students):
    total = 0
    for student in students:
        total = total + student["score"]

        average = total / len(students)
    return average

def get_pass_students(students):
    pass_students = []
    for student in students:
        if student["score"] >= 60 and student["attendance"] >= 80:
            pass_students.append(student)

    return pass_students