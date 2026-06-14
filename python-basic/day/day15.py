def total_scores(scores):
    total = 0

    for score in scores:
        total = total + score

    return total

def average_score(scores):
    total = total_scores(scores)
    average = total / len(scores)

    return average

def score_level(average):
    if average >=80:
        return "good"
    elif average >= 60:
        return "pass"
    else:
        return "fail"
    
scores = []

student = int(input("enter student number: "))

for number in range(1, student + 1):
    score = float(input(f"enter student {number} score: "))
    scores.append(score)

total = total_scores(scores)
average = average_score(scores)
level = score_level(average)

print(total)
print(average)
print(level)
