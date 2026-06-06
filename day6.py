name = input("enter your name: ")
score = float(input("enter your score: "))
attendance = float(input("enter your attendance: "))
bonus = input("Do you have bonus? yes/no: ")

print("---result---")
print("your name:", name)
print("your score:", score)
print("your attendance:", attendance)
print("you have bonus or not:", bonus)

if score >= 60 and (attendance >= 80 or bonus == "yes"):
    print("pass")
else:
    print("fail")
if score >= 90 and attendance >= 90 and bonus == "yes":
    print("excellent")
else:
    print("normal")