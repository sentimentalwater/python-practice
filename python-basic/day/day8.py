day = 1
total_day = int(input("enter your learning day:"))

while day <= total_day:
    print("day", day, "finishied")
    day = day + 1

print("all days finished")


password = ""
while password != "123456":
    password = input("enter your password:")

print("welcome!")