scores = []
student_number = int(input("enter student number: "))

for number in range(1, student_number + 1):
    score = float(input(f"enter student {number} score: "))
    scores.append(score)

excellent_scores = []
pass_scores = []
fail_scores = []

for score in scores:
    if score >= 90:
        excellent_scores.append(score)
    elif score >= 60:
        pass_scores.append(score)
    else:
        fail_scores.append(score)

excellent_count = len(excellent_scores)
pass_count = len(pass_scores)
fail_count = len(fail_scores)
pass_rate = len(pass_scores) / len(scores) * 100

print("result")
print("scores: ", scores)
print("excellent_scores: ", excellent_scores)
print("pass_scores: ", pass_scores)
print("fail_scores: ", fail_scores)
print(excellent_count)
print(pass_count)
print(fail_count)
print("pass rate: ", pass_rate, "%")