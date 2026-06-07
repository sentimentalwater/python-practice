scores = []
student_number = int(input("enter student number: "))

for number in range(1, student_number + 1):
    score = float(input(f"enter student {number} score: "))
    scores.append(score)

total_scores = 0

for score in scores:
    total_scores = total_scores + score

average_score = total_scores / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

if average_score >= 90:
    print("excellent")
elif average_score >= 80:
    print ("good")
elif average_score >= 60:
    print("pass")
else:
    print("fail")

print("result")
print(scores)
print(total_scores)
print(average_score)
print(highest_score)
print(lowest_score)