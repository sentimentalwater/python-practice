def get_scores():
    student = int(input("student number: "))
    scores = []
    for number in range(1, student + 1):
        score = float(input(f"enter student {number} score: "))
        scores.append(score)

    return scores

def get_total(scores):
    total = 0
    for score in scores:
        total = total + score

    return total

def get_average(total, scores):
    average = total / len(scores)

    return average

def get_level(average):
    if average >= 80:
        return "good"
    elif average >=60:
        return "pass"
    else:
        return "fail"

def get_maxmin(scores):
    highest_score = max(scores)
    lowest_score = min(scores)

    return highest_score, lowest_score

def get_result(scores, total, average, maxmin, level):
    print(scores)
    print(total)
    print(average)
    print(maxmin)
    print(level)
    
scores = get_scores()
total = get_total(scores)
average = get_average(total, scores)
maxmin = get_maxmin(scores)
level = get_level(average)

get_result(scores, total, average, maxmin, level)