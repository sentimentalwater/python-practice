def get_infor():
    students =[]
    total_students = int(input("enter student number: "))
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
    return students

def provide_infor(students):
    for student in students:
        for key, value in student.items():
            print(key + ":", value)


def get_passstudent(students):
    pass_student = []
    for student in students:
        if student["score"] >= 60 and student["attendance"] >= 80:
            pass_student.append(student)
    return pass_student

def get_average(students):
    total = 0
    for student in students:
        total = total + student["score"]

    average = total / len(students)
    return average

def get_highest_atudent(students):
    highest_student = students[0]
    for student in students:
        if student["score"] > highest_student["score"]:
            highest_student = student

    return highest_student

students = get_infor()
provide_infor(students)
pass_students = get_passstudent(students)
average = get_average(students)
highest_student = get_highest_atudent(students)


print(students)
print(pass_students)
print(average)
print(highest_student)