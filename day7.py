name = input("your name:").strip()
score = float(input("your score:"))
attendance = float(input("your attendance rate:"))
bonus = input("Do you have bonus? yes/no").strip().lower()

print("result")
print(name)
print(score)
print(attendance)
print(bonus)

if score >= 60 or bonus == "yes":
    print("pass")
else:
    print("fail")
if score >= 90 and attendance >=80:
    print("excellent")
else:
    print("normal")