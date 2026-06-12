def read_students():
    students = []

    try:
        with open ("students.csv", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                part = line.split(",")

                try:
                    student = {
                        "name": part[0],
                        "score": float(part[1]),
                        "attendance": float(part[2])
                    }
                    students.append(student)

                except IndexError:
                    print("Invalid line format: ", line)

                except ValueError:
                    print("Invalid number in line: ", line)

    except FileNotFoundError:
        print("no found this csv")

    return students

def get_infor(students):
    for student in students:
        print("-student-")
        print(student["name"])
        print(student["score"])
        print(student["attendance"])

students = read_students()
get_infor(students)