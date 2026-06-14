total_days = int(input("enter learning day: "))
total_hours = 0

for day in range(1, total_days +1):
    hours = float(input("enter hours for day" + str(day) +":"))
    total_hours = total_hours + hours

print("--result--")
print("total days: ", total_days)
print("total hours: ", total_hours)
print("average hours: ", total_hours / total_days)