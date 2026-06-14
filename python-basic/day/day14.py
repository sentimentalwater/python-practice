def student_infor(student):
    print("name: ", student["name"])
    print("score: ", student["score"])

    if student["score"] >= 60:
        print("pass")
    else:
        print("fail")

print("---------------")

students = []

total_students = int(input("enter number: "))

for number in range(1, total_students + 1):
    name = input(f"enter student {number} name: ").strip()
    score = float(input(f"enter student {number} score: "))

    student = {
        "name": name,
        "score": score
    }
    
    students.append(student)


for student in students:
    student_infor(student)