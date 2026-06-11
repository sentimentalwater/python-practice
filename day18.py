def student_infor(text):
    part = text.split(",")
    name = part[0]
    score = float(part[1])
    attendance = float(part[2])

    student = {
        "name": name,
        "score": score,
        "attendance": attendance
    }
    return student

def get_result(student):
    print("name: ", student["name"])
    print("score: ", student["score"])
    print("attendance: ", student["attendance"])

text = input("enter text like Alex,85,90: ").strip()

student = student_infor(text)

get_result(student)


text1 = "Python Git VSCode"
text1_new = text.split()
print(text1_new)


