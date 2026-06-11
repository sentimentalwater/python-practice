def check_student(students):
    for student in students:
        for key, value in student.items():
            print(key, ":", value)

students = [
    {"name": "Alex", "score": 99, "attendance": 80},
    {"name": "Bob", "score": 88, "attendance": 90},
    {"name": "Cindy", "score": 77, "attendance": 90}
]

check_student(students)