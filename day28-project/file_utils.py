def save_students(students):
    with open ("students.csv", "w", encoding="utf-8") as file:
        for student in students:
            file.write(f"{student['name']},{student['score']},{student['attendance']}\n")

def read_students():
    students = []
    try:
        with open ("students.csv", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")

                try:
                    student = {
                        "name": parts[0],
                        "score": float(parts[1]),
                        "attendance": float(parts[2])
                    }
                    students.append(student)
                except IndexError:
                    print("", line)
                except ValueError:
                    print("", line)
    except FileNotFoundError:
        print("")
    return students