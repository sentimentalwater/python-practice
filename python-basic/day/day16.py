def check_result(score, attendance, pass_score = 65, pass_attendance = 85):
    if score >= pass_score and attendance >= pass_attendance:
        return "pass"
    else:
        return "fail"
    
def check_level(score):
    if score >= 80:
        return "good"
    elif score >=60:
        return "pass"
    else:
        return "fail"
    
name = input("your name: ").strip().lower()
score = float(input("your score: "))
attendance = float(input("your attandance: "))

result = check_result(score, attendance)
level = check_level(score)

print(name)
print(score)
print(attendance)
print(result)
print(level)