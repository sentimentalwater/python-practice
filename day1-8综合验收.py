password = ""
while password != "123456":
    password = input("enter password:")
print("welcome")

name = input("enter your name:").strip()
score = float(input("enter your score:"))
attendance = float(input("enter your attendance rate:"))
bonus = input("Do you have bonus? yes/no").strip().lower()

print("---result---")
print("name:", name)
print("score:", score)
print("attendance:", attendance)
print("have bonus or not:", bonus)

if score >= 60 and attendance >= 80 or bonus == "yes":
    print("pass")
else:
    print("fail")

if score >= 90 and attendance >= 90 and bonus == "yes":
    print("excellent")
elif score >= 80:
    print("good")
elif score >= 60:
    print("pass")
else:
    print("fail")
