name = input("enter your name:")
daily_hours = float(input("enter your time:"))
day = int(input("enter your day:"))

weekly_hours = daily_hours*7
total_hours = daily_hours*day

print("---learning result---")
print("your name:", name)
print("hours:", daily_hours)
print("day:", day)
print("weekly hours:", weekly_hours + 1)
print("total hours:", total_hours + 1)