def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("please enter a number:")

def get_students():
    students = []
    student_number = int(get_number("enter student number:"))
    for number in range(1, student_number + 1):
        name = input(f"student {number} name:").strip()
        score = get_number(f"enter student {number} score:")
        attendance = get_number(f"enter student {number} attendance:")

        student = {
            "name": name,
            "score": score,
            "attendance": attendance
        }
        students.append(student)

    return students
    
def print_students(students):
    for student in students:
        print("--student--")
        print("name:", student["name"])
        print("score:", student["score"])
        print("attendance:", student["attendance"])

def get_average(students):
    total = 0
    for student in students:
        total = total + student["score"]
    average = total / len(students)
    return average

def get_passer(students):
    passers = []
    for student in students:
        if student["score"] >= 60 and student["attendance"] >= 80:
            passers.append(student)
    return passers

def get_highest_person(students):
    highest_person = students[0]
    for student in students:
        if student["score"] >= highest_person["score"]:
            highest_person = student
    return highest_person
