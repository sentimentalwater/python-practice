def read_file():
    students = []
    with open ("students.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            parts = line.split(",")

            name = parts[0]
            score = float(parts[1])
            attendance = float(parts[2])

            student = {
            "name": name,
            "score": score,
            "attendance": attendance
            }
            students.append(student)

    return students

def print_students(students):
    for student in students:
        print("----- Student -----")
        print("Name:", student["name"])
        print("Score:", student["score"])
        print("Attendance:", student["attendance"])


students = read_file()
print_students(students)
