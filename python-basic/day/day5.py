name = input("your name:")
score = float(input("your score:"))

print("---score result---")
print("your name:", name)
print("your score:", score)

if score >= 90:
    print("excellent")
elif score >= 80:
    print("good")
elif score >= 70:
    print("medium")
elif score >= 60:
    print("pass")
else:
    print("fail")