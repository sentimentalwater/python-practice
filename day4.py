name = input("your name:")
score = float(input("your score:"))

print("---result---")
print("your name:", name)
print("your score:", score)

if score >= 60:
    print("status: pass")
else:
    print("status: fail")

if score >= 90:
    print("level: excellent")
else:
    print("level: not excellent")