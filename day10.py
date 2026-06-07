student_scores = []
total_students = int(input("enter student number: "))

for number in range(1, total_students + 1):
    score = input(f"enter student {number} score: ").strip()
    student_scores.append(score)

print("--scores--")
print(student_scores)
print(len(student_scores))