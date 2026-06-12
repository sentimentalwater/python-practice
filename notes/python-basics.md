
## 今日主题
Python 基础：变量与输出

## 核心概念

### 1. .py 文件
`.py` 文件是 Python 代码文件，可以用终端运行。

运行命令：

```bash
python day1.py
```

### 2. 变量
变量用于保存数据。

```python
name = "Alex"
major = "computer science"
goal = "have strong programming ability"
```

结构：

```text
变量名 = 数据
```

### 3. print()
`print()` 用于把内容输出到终端。

```python
print(name)
print(major)
print(goal)
```

## 易错点

### 1. 引号和变量的区别

```python
print("name")  # 输出普通文本 name
print(name)    # 输出变量 name 里面的内容
```

结论：

```text
引号里面的是普通文本；没有引号的是变量名。
```

## 今日复盘
我理解了：
- 变量可以保存数据。
- `print()` 可以输出内容。
- `print("name")` 和 `print(name)` 不一样。
- `python` 和 `bash` 用于高亮。代码；终端命令



# Day 2：input() 用户输入

## 概念
`input()` 用于接收用户在终端输入的内容。

## 示例

```python
name = input("Enter your name: ")
print(name)
```

## 完整代码

```python
name = input("Enter your name: ")
major = input("Enter your major: ")
goal = input("Enter your learning goal: ")

print("----- User Information -----")
print("Name:", name)
print("Major:", major)
print("Goal:", goal)
```

## 要点
- `input()` 会等待用户输入。
- 输入的内容可以保存到变量里。
- `input()` 里的文字是提示语。
- `print("Name:", name)` 可以同时输出说明文字和变量内容。

## 易错点
- `print("name")` 输出普通文本。
- `print(name)` 输出变量里的内容。
- `input()` 后面必须有括号。
- 提示语要放在引号里。

## 今日误区预防
- 不要把变量名写进引号。
- 不要把终端命令写进 Python 文件。



# Day 3：int() / float() 类型转换

## 概念
`input()` 得到的内容默认是字符串。  
做数学计算前，需要用 `int()` 或 `float()` 转成数字。

## 示例

```python
age = int(input("Enter your age: "))
print(age + 1)
```

```python
hours = float(input("Enter study hours: "))
print(hours)
```

## 完整代码

```python
name = input("Enter your name: ")
daily_hours = float(input("How many hours do you study programming every day? "))
days = int(input("How many days will you keep learning? "))

total_hours = daily_hours * days

print("----- Study Result -----")
print("Name:", name)
print("Daily hours:", daily_hours)
print("Days:", days)
print("Total hours:", total_hours)
```

## 要点
- `input()` 默认得到字符串。
- `int()` 用于整数。
- `float()` 用于小数。
- 数学计算前要先转换类型。

## 易错点
- `input()` 得到的 `"18"` 不是数字 `18`。
- 小数不能直接用 `int()` 转换。
- 输入非数字内容时，`int()` / `float()` 会报 `ValueError`。


# Day 4：if / else 条件判断

## 概念
`if / else` 用于让程序根据条件执行不同代码。

## 示例

```python
score = float(input("Enter your score: "))

if score >= 60:
    print("Pass")
else:
    print("Fail")
```

## 完整代码

```python
name = input("Enter your name: ")
score = float(input("Enter your score: "))

print("----- Result -----")
print("Name:", name)
print("Score:", score)

if score >= 60:
    print("Status: Pass")
else:
    print("Status: Fail")
```

## 要点
- `if` 表示如果。
- `else` 表示否则。
- `if` 条件后面要加冒号 `:`。
- Python 用缩进表示代码块。
- `=` 是赋值，`==` 是判断相等。

## 常用比较符

```text
>    大于
<    小于
>=   大于等于
<=   小于等于
==   等于
!=   不等于
```

## 易错点
- 忘记写冒号 `:`。
- `if` 下面的代码忘记缩进。
- 把 `==` 写成 `=`。
- 输入分数后忘记用 `float()` 或 `int()` 转数字。
```



# Day 5：elif 多分支判断

## 概念
`elif` 用于处理多个条件，意思是“否则如果”。

## 示例

```python
score = float(input("Enter your score: "))

if score >= 90:
    print("Excellent")
elif score >= 80:
    print("Good")
elif score >= 60:
    print("Pass")
else:
    print("Fail")
```

## 要点
- `if` 判断第一个条件。
- `elif` 判断其他条件。
- `else` 处理以上条件都不成立的情况。
- 程序从上往下判断，满足一个条件后就停止。

## 易错点
- `if`、`elif`、`else` 后面都要加冒号 `:`。
- 条件下面的代码要缩进。
- 判断成绩等级时，高分条件要写在前面。

## 今日代码结构

```text
输入分数 → 从高到低判断等级 → 输出结果
```


# Day 6：and / or 多条件判断

## 概念
`and / or` 用于判断多个条件。

## 示例

```python
if score >= 60 and attendance >= 80:
    print("Pass")
else:
    print("Fail")
```

```python
if score >= 60 or attendance >= 95:
    print("Pass")
else:
    print("Fail")
```

## 完整代码

```python
name = input("Enter your name: ")
score = float(input("Enter your score: "))
attendance = float(input("Enter your attendance rate: "))

print("----- Course Result -----")
print("Name:", name)
print("Score:", score)
print("Attendance:", attendance)

if score >= 60 and attendance >= 80:
    print("Result: Pass")
else:
    print("Result: Fail")
```

## 要点
- `and`：两个条件都成立，整体才成立。
- `or`：至少一个条件成立，整体就成立。
- 多条件判断仍然要注意冒号和缩进。

## 易错点
- `and` 和 `or` 不要混淆。
- 条件两边都要写完整。
- 不要写成 `score >= 60 and attendance`。
- 正确写法是 `score >= 60 and attendance >= 80`。


# Day 7：strip() / lower() 处理字符串输入

## 概念
`strip()` 去掉字符串两边空格。  
`lower()` 把英文转成小写。

## 示例

```python
text = " YES "
print(text.strip().lower())
```

输出：

```text
yes
```

## 完整代码

```python
name = input("Enter your name: ").strip()
score = float(input("Enter your score: "))
attendance = float(input("Enter your attendance: "))
bonus = input("Do you have bonus? yes/no: ").strip().lower()

if score >= 60 and (attendance >= 80 or bonus == "yes"):
    print("Result: Pass")
else:
    print("Result: Fail")
```

## 要点
- `input()` 得到的是字符串。
- 用户输入可能有大小写和空格问题。
- `.strip().lower()` 可以让输入更稳定。
- 常用于处理 yes/no 这类输入。

## 易错点
- `bonus == "yes"` 只能识别小写 yes。
- 用户输入 `YES`、`Yes`、` yes ` 时，直接判断可能失败。
- 推荐写法：`input(...).strip().lower()`


# Day 8：while 循环

## 概念
`while` 用于重复执行代码。只要条件成立，就继续循环。

## 示例

```python
count = 1

while count <= 5:
    print(count)
    count = count + 1
```

## 完整代码

```python
day = 1
total_days = int(input("Enter total learning days: "))

while day <= total_days:
    print("Day", day, "completed")
    day = day + 1

print("All days completed.")
```

## 要点
- `while` 后面写条件。
- 条件后面要加冒号 `:`。
- 循环体要缩进。
- 循环变量要变化，否则可能死循环。

## 易错点
- 忘记写冒号。
- 忘记缩进。
- 忘记写 `count = count + 1`，导致死循环。
- `while count <= 5:` 会在条件为 True 时一直执行。


# Day 9：for 循环 + range()

## 概念
`for` 用于按次数循环。  
`range()` 用于生成数字范围。

## 示例

```python
for number in range(1, 6):
    print(number)
```

输出：

```text
1
2
3
4
5
```

## range()
```python
range(5)        # 0 到 4
range(1, 6)     # 1 到 5
range(1, 10, 2) # 1, 3, 5, 7, 9
```

## 累加

```python
total = 0

for number in range(1, 6):
    total = total + number

print(total)
```

## 完整代码

```python
total_days = int(input("Enter total learning days: "))
total_hours = 0

for day in range(1, total_days + 1):
    hours = float(input("Enter study hours for day " + str(day) + ": "))
    total_hours = total_hours + hours

print("Total days:", total_days)
print("Total hours:", total_hours)
print("Average hours:", total_hours / total_days)
```

## 要点
- `range()` 包含开始，不包含结束。
- `range(1, 6)` 输出 1 到 5。
- `for` 下面的代码要缩进。
- `total = total + hours` 表示不断累加。
- `str(day)` 把数字转成字符串，方便和文字拼接。

## 易错点
- 忘记冒号 `:`。
- 忘记缩进。
- 想输出 1 到 5，却写成 `range(1, 5)`。
- 数字和字符串不能直接用 `+` 拼接，需要 `str()`。


# Day 10：list 列表基础

## 概念
`list` 用于保存一组数据。

## 示例

```python
names = ["Alex", "Bob", "Cindy"]

print(names[0])
print(names[1])
print(names[2])
```

## 常用操作

```python
names = ["Alex", "Bob"]

names.append("Cindy")
print(names)

print(len(names))
```

## 完整代码

```python
students = []

total_students = int(input("Enter number of students: "))

for number in range(1, total_students + 1):
    name = input(f"Enter student {number} name: ").strip()
    students.append(name)

print("----- Student List -----")
print(students)
print("Total students:", len(students))
```

## 要点
- 列表可以保存多个数据。
- 索引从 `0` 开始。
- `append()` 用于添加元素。
- `len()` 用于获取列表长度。
- 空列表写作 `[]`。

## 易错点
- 第一个元素是 `names[0]`，不是 `names[1]`。
- `append()` 后面要有括号。
- `students.append(name)` 是把变量 `name` 的内容加入列表。
- 不要写成 `students = students.append(name)`。


# Day 11：列表遍历 + 统计

## 概念
遍历列表：把列表里的元素一个个取出来处理。

## 示例

```python
scores = [85, 90, 76]

for score in scores:
    print(score)
```

## 累加

```python
total_score = 0

for score in scores:
    total_score = total_score + score
```

## 完整代码

```python
scores = []

total_students = int(input("Enter student number: "))

for number in range(1, total_students + 1):
    score = float(input(f"Enter student {number} score: "))
    scores.append(score)

total_score = 0

for score in scores:
    total_score = total_score + score

average_score = total_score / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

print("Scores:", scores)
print("Total score:", total_score)
print("Average score:", average_score)
print("Highest score:", highest_score)
print("Lowest score:", lowest_score)
```

## 要点
- `for score in scores` 会依次取出列表中的每个分数。
- `total_score = total_score + score` 表示累加。
- `len(scores)` 获取列表长度。
- `max(scores)` 获取最大值。
- `min(scores)` 获取最小值。

## 易错点
- 输入分数时要用 `float()`，否则保存的是字符串。
- `score` 是循环临时变量，不需要提前创建。
- `len(scores)` 不能为 0，否则平均分计算会出错。
- `scores.append(score)` 是把分数加入列表。


# Day 12：列表筛选 + 条件统计

## 概念
列表筛选：遍历列表，用 `if` 判断，把符合条件的数据放进新列表。

## 示例

```python
scores = [85, 45, 90, 58, 76]

passed_scores = []
failed_scores = []

for score in scores:
    if score >= 60:
        passed_scores.append(score)
    else:
        failed_scores.append(score)

print(passed_scores)
print(failed_scores)
```

## 计数

```python
pass_count = 0

for score in scores:
    if score >= 60:
        pass_count += 1
```

`pass_count += 1` 等于：

```python
pass_count = pass_count + 1
```

## 完整代码

```python
scores = []

total_students = int(input("Enter student number: "))

for number in range(1, total_students + 1):
    score = float(input(f"Enter student {number} score: "))
    scores.append(score)

passed_scores = []
failed_scores = []

for score in scores:
    if score >= 60:
        passed_scores.append(score)
    else:
        failed_scores.append(score)

pass_count = len(passed_scores)
fail_count = len(failed_scores)
pass_rate = pass_count / len(scores) * 100

print("All scores:", scores)
print("Passed scores:", passed_scores)
print("Failed scores:", failed_scores)
print("Pass count:", pass_count)
print("Fail count:", fail_count)
print("Pass rate:", pass_rate, "%")
```

## 要点
- `for score in scores` 遍历列表。
- `if score >= 60` 判断是否及格。
- `append()` 把符合条件的数据加入新列表。
- `len()` 可以统计列表元素数量。
- `+= 1` 是累加简写。

## 易错点
- `passed_scores` 和 `failed_scores` 要先创建为空列表。
- `append()` 要放在循环内部。
- `pass_rate = pass_count / len(scores) * 100` 中，`len(scores)` 不能为 0。
- 输入分数要用 `float()`。



# Day 13：dict 字典基础

## 概念
`dict` 用 key-value 保存数据。

```python
student = {
    "name": "Alex",
    "score": 90
}
```

## 读取

```python
print(student["name"])
print(student["score"])
```

## 修改 / 新增

```python
student["score"] = 95
student["attendance"] = 90
```

## list + dict

```python
students = []

student = {
    "name": "Alex",
    "score": 90,
    "attendance": 95
}

students.append(student)
```

## 完整代码

```python
students = []

total_students = int(input("Enter student number: "))

for number in range(1, total_students + 1):
    name = input(f"Enter student {number} name: ").strip()
    score = float(input(f"Enter student {number} score: "))
    attendance = float(input(f"Enter student {number} attendance: "))

    student = {
        "name": name,
        "score": score,
        "attendance": attendance
    }

    students.append(student)

for student in students:
    print("Name:", student["name"])
    print("Score:", student["score"])
    print("Attendance:", student["attendance"])

    if student["score"] >= 60 and student["attendance"] >= 80:
        print("Result: Pass")
    else:
        print("Result: Fail")
```

## 要点
- `dict` 用 `{}`。
- 数据结构是 `"key": value`。
- 用 `student["name"]` 读取数据。
- key 通常用字符串。
- 多个 dict 可以放进 list。

## 易错点
- key 要加引号，例如 `"name"`。
- 读取不存在的 key 会报错。
- `student["score"] = 95`：key 存在是修改，不存在是新增。
- `students.append(student)` 是把整个学生字典加入列表。


# Day 14：函数 def 基础

## 概念
函数用于把一段代码打包，需要时调用。

## 示例

```python
def say_hello():
    print("Hello")

say_hello()
```

## 参数

```python
def greet(name):
    print("Hello,", name)

greet("Alex")
```

## 结合 dict

```python
def print_student(student):
    print("Name:", student["name"])
    print("Score:", student["score"])
    print("Attendance:", student["attendance"])

student = {
    "name": "Alex",
    "score": 85,
    "attendance": 90
}

print_student(student)
```

## 完整代码

```python
def print_student(student):
    print("Name:", student["name"])
    print("Score:", student["score"])
    print("Attendance:", student["attendance"])

    if student["score"] >= 60 and student["attendance"] >= 80:
        print("Result: Pass")
    else:
        print("Result: Fail")

    print("-----")
```

## 要点
- `def` 用于定义函数。
- 函数名后面要有 `()`。
- 函数体要缩进。
- 定义函数不等于执行函数。
- 调用函数要写 `函数名()`。
- 参数是调用函数时传进去的数据。

## 易错点
- 只写 `def` 不调用，函数不会执行。
- 调用函数时不要忘记括号。
- 函数要先定义，再调用。
- 参数名只在函数内部使用。


# Day 15：return 返回值

## 概念
`return` 用于把函数内部的结果返回到函数外部。

## print 和 return

```python
print(result)   # 显示结果
return result   # 返回结果
```

## 示例

```python
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(3, 5)
print(total)
```

## 判断函数

```python
def check_pass(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"
```

## 完整代码

```python
def calculate_total(scores):
    total = 0

    for score in scores:
        total = total + score

    return total


def calculate_average(scores):
    total = calculate_total(scores)
    average = total / len(scores)
    return average


def check_level(average_score):
    if average_score >= 90:
        return "Excellent"
    elif average_score >= 80:
        return "Good"
    elif average_score >= 60:
        return "Pass"
    else:
        return "Fail"
```

## 要点
- `return` 后面的值会返回给函数调用处。
- 调用函数后，可以用变量接住返回值。
- `print()` 只是显示，`return` 才能让结果继续被使用。
- 函数可以调用另一个函数。

## 易错点
- 只写 `return` 不 `print`，终端不会自动显示结果。
- `return` 后面的代码通常不会继续执行。
- 调用函数时要用变量接住结果，例如 `total = calculate_total(scores)`。


# Day 16：函数参数进阶

## 概念
函数可以接收多个参数，也可以设置默认参数。

## 多个参数

```python
def show_student(name, score, attendance):
    print("Name:", name)
    print("Score:", score)
    print("Attendance:", attendance)

show_student("Alex", 85, 90)
```

## 关键字参数

```python
show_student(name="Alex", score=85, attendance=90)
```

## 默认参数

```python
def check_pass(score, pass_score=60):
    if score >= pass_score:
        return "Pass"
    else:
        return "Fail"
```

## 完整代码

```python
def check_result(score, attendance, pass_score=60, pass_attendance=80):
    if score >= pass_score and attendance >= pass_attendance:
        return "Pass"
    else:
        return "Fail"


def check_level(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"
```

## 要点
- 参数是函数接收的外部数据。
- 多个参数按顺序传入。
- 关键字参数可以明确指定参数名。
- 默认参数可以让函数更灵活。
- 默认参数写在普通参数后面。

## 易错点
- 参数顺序写错，结果可能不报错但逻辑错。
- 默认参数不要写在普通参数前面。
- 调用函数时，括号里放真实数据。
- 定义函数时，括号里放参数名。



# Day 17：函数拆分综合练习

## 概念
函数拆分：把一个长程序拆成多个函数，一个函数只负责一件事。

## 常见拆分

```python
def get_scores():
    ...

def calculate_average(scores):
    ...

def check_level(average):
    ...

def print_result(scores, average, level):
    ...
```

## 完整流程

```python
scores = get_scores()
average = calculate_average(scores)
level = check_level(average)

print_result(scores, average, level)
```

## 示例代码

```python
def calculate_average(scores):
    total = 0

    for score in scores:
        total = total + score

    average = total / len(scores)

    return average
```

## 要点
- 函数定义不会自动执行。
- 函数调用才会执行。
- `return` 把结果交给函数外部。
- 一个函数尽量只负责一件事。
- 主程序应该像流程说明一样清楚。

## 易错点
- 调用函数时不要忘记括号。
- 函数需要什么数据，括号里就传什么数据。
- 函数返回的结果要用变量接住。
- 修改函数参数后，调用函数的地方也要同步修改。


# Day 18：字符串方法补充

## split()

把字符串拆成列表。

```python
text = "Alex,85,90"
parts = text.split(",")

print(parts)
```

## join()

把字符串列表合成字符串。

```python
names = ["Alex", "Bob", "Cindy"]

text = ",".join(names)

print(text)
```

## replace()

替换字符串内容。

```python
text = "I like Java"

new_text = text.replace("Java", "Python")

print(new_text)
```

## startswith()

判断字符串开头。

```python
filename = "report.txt"

print(filename.startswith("report"))
```

## endswith()

判断字符串结尾。

```python
filename = "report.txt"

print(filename.endswith(".txt"))
```

## 示例：解析学生信息

```python
text = "Alex,85,90"
parts = text.split(",")

name = parts[0]
score = float(parts[1])
attendance = float(parts[2])
```

## 要点

- `split()`：字符串 → 列表
- `join()`：列表 → 字符串
- `replace()`：替换内容
- `startswith()`：判断开头
- `endswith()`：判断结尾
- `split()` 拆出来的数字仍然是字符串，需要 `int()` 或 `float()`

## 易错点

- `split()` 返回列表，要用索引取值。
- `parts[1]` 是字符串，不是数字。
- `join()` 只能直接连接字符串列表。
- `",".join(names)` 前面的逗号是连接符。



# Day 19：遍历 dict 字典

## keys()

遍历字典所有 key。

```python
for key in student.keys():
    print(key)
```

## values()

遍历字典所有 value。

```python
for value in student.values():
    print(value)
```

## items()

同时遍历 key 和 value。

```python
for key, value in student.items():
    print(key, value)
```

## 示例

```python
student = {
    "name": "Alex",
    "score": 85,
    "attendance": 90
}

for key, value in student.items():
    print(key + ":", value)
```

## list + dict 遍历

```python
students = [
    {"name": "Alex", "score": 85},
    {"name": "Bob", "score": 75}
]

for student in students:
    for key, value in student.items():
        print(key + ":", value)
```

## 要点

- `keys()` 取所有 key。
- `values()` 取所有 value。
- `items()` 同时取 key 和 value，最常用。
- 外层循环遍历列表，内层循环遍历字典。

## 易错点

- `items()` 要写成 `for key, value in student.items():`
- `key + ":"` 要求 key 是字符串。
- `print(key + ":", value)` 比 `print(key + ":" + value)` 更安全，因为 value 可能是数字。


# Day 20：list + dict 综合练习

## 核心结构

```python
students = [
    {"name": "Alex", "score": 90, "attendance": 95},
    {"name": "Bob", "score": 75, "attendance": 70}
]
```

## 创建学生列表

```python
students = []

student = {
    "name": name,
    "score": score,
    "attendance": attendance
}

students.append(student)
```

## 遍历所有学生

```python
for student in students:
    for key, value in student.items():
        print(key + ":", value)
```

## 筛选学生

```python
passed_students = []

for student in students:
    if student["score"] >= 60 and student["attendance"] >= 80:
        passed_students.append(student)
```

## 计算平均分

```python
total_score = 0

for student in students:
    total_score = total_score + student["score"]

average_score = total_score / len(students)
```

## 找最高分学生

```python
top_student = students[0]

for student in students:
    if student["score"] > top_student["score"]:
        top_student = student
```

## 要点

- `students` 是列表。
- 每个 `student` 是字典。
- 先遍历 list，再处理 dict。
- `student["score"]` 用来取当前学生的分数。
- `students.append(student)` 把一个学生加入学生列表。
- 函数拆分可以让程序结构更清楚。

## 易错点

- list 没有 `.items()`，dict 才有。
- `students[0]` 是第一个学生字典。
- `student["score"]` 不能写成 `students["score"]`。
- 函数里算出来的结果，后面要用就必须 `return`。


# Day 21：文件写入 txt

## open() 写入文件

```python
with open("students.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python")
```

## w 模式

```python
"w"
```

覆盖写入。原文件内容会被清空。

## a 模式

```python
"a"
```

追加写入。新内容会加到文件末尾。

## 换行

```python
file.write("Alex\n")
file.write("Bob\n")
```

`\n` 表示换行。

## 写入数字

```python
score = 90

file.write(str(score))
```

`write()` 只能直接写字符串，数字要用 `str()` 转换。

## 写入多个学生

```python
with open("students.txt", "w", encoding="utf-8") as file:
    for student in students:
        file.write("Name: " + student["name"] + "\n")
        file.write("Score: " + str(student["score"]) + "\n")
```

## 要点

- `with open(...) as file:` 是打开文件的常用写法。
- `file.write()` 用来写入内容。
- `w` 会覆盖原内容。
- `a` 会追加内容。
- 多行内容要加 `\n`。
- 写入数字要先转成字符串。

## 易错点

- 忘记加 `\n`，内容会挤在一行。
- `write()` 不能直接写数字。
- `w` 模式会覆盖原文件。
- 文件通常会生成在当前运行目录下。



# Day 22：文件读取 txt

## 读取全部内容

```python
with open("students.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

## r 模式

```python
"r"
```

读取模式。文件必须已经存在。

## 逐行读取

```python
with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        print(line)
```

## readlines()

```python
with open("students.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

会把所有行读成列表。

## strip()

```python
line = line.strip()
```

去掉行首行尾空格和换行符 `\n`。

## split()

```python
line = "Alex,90,95"
parts = line.split(",")

name = parts[0]
score = float(parts[1])
attendance = float(parts[2])
```

## 示例：读取学生数据

```python
students = []

with open("students.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        parts = line.split(",")

        student = {
            "name": parts[0],
            "score": float(parts[1]),
            "attendance": float(parts[2])
        }

        students.append(student)
```

## 要点

- `read()` 读取全部内容。
- `readline()` 一次读取一行。
- `readlines()` 读取所有行，返回列表。
- `for line in file` 最常用。
- `strip()` 去掉换行。
- `split(",")` 可以把一行文本拆成多个字段。

## 易错点

- `r` 模式下文件不存在会报错。
- 读取出来的内容默认是字符串。
- `parts[1]` 是字符串，要计算必须用 `float()`。
- 文件要和 `.py` 文件在同一个运行目录下，或者写清楚路径。


# Day 23：CSV 文件基础

## CSV 是什么

CSV 是用逗号分隔数据的文件。

```text
Alex,90,95
Bob,75,70
```

一行是一条数据，逗号分隔不同字段。

## 写入 CSV

```python
with open("students.csv", "w", encoding="utf-8") as file:
    for student in students:
        file.write(f"{student['name']},{student['score']},{student['attendance']}\n")
```

## 读取 CSV

```python
students = []

with open("students.csv", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        parts = line.split(",")

        student = {
            "name": parts[0],
            "score": float(parts[1]),
            "attendance": float(parts[2])
        }

        students.append(student)
```

## 核心流程

```text
写入：dict/list → CSV 文本
读取：CSV 文本 → split(",") → dict/list
```

## 要点

- CSV 本质上是有规则的文本文件。
- 一行通常表示一条数据。
- 逗号用来分隔字段。
- 读取出来的内容默认是字符串。
- 分数、出勤率要用 `float()` 转成数字。

## 易错点

- 忘记 `\n`，多条数据会挤在一行。
- `parts[1]` 是字符串，不是数字。
- 文件名要和代码里一致。
- 当前代码只能读取固定格式：`name,score,attendance`。


# Day 24：try / except 异常处理

## 基本写法

```python
try:
    score = float(input("Enter score: "))
except ValueError:
    print("Invalid input.")
```

## 含义

- `try`：放可能出错的代码
- `except`：放出错后的处理方式

## while + try

```python
while True:
    try:
        score = float(input("Enter score: "))
        break
    except ValueError:
        print("Please enter a number.")
```

## 封装输入函数

```python
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Please enter a number.")
```

## 文件不存在

```python
try:
    with open("students.csv", "r", encoding="utf-8") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found.")
```

## CSV 格式错误

```python
try:
    student = {
        "name": parts[0],
        "score": float(parts[1]),
        "attendance": float(parts[2])
    }
except IndexError:
    print("Invalid line format.")
except ValueError:
    print("Invalid number.")
```

## 常见异常

- `ValueError`：数值转换失败
- `FileNotFoundError`：文件不存在
- `IndexError`：索引不存在
- `NameError`：变量名不存在

## 要点

- `try` 里写可能出错的代码。
- `except` 里写错误处理。
- 不要用 try 掩盖所有问题，要知道自己在处理什么错误。
- 输入、文件读取、格式转换很适合用 try/except。


# Day 25：import 模块基础

## import 是什么

`import` 用来导入模块。模块可以理解为别人已经写好的工具包。

## random

```python
import random

number = random.randint(1, 10)
print(number)
```

## random.choice()

```python
import random

names = ["Alex", "Bob", "Cindy"]
name = random.choice(names)

print(name)
```

## datetime

```python
import datetime

today = datetime.date.today()
print(today)
```

## os

```python
import os

print(os.getcwd())
```

## from import

```python
from random import randint

number = randint(1, 10)
```

## 示例：学习日志

```python
import datetime

today = datetime.date.today()

with open("study_log.txt", "a", encoding="utf-8") as file:
    file.write(f"{today},Python import,2\n")
```

## 要点

- `import` 是导入模块。
- 模块是别人写好的工具包。
- `random` 用来生成随机数或随机选择。
- `datetime` 用来处理日期和时间。
- `os.getcwd()` 可以查看当前运行目录。
- `a` 模式用于追加写入。

## 易错点

- `import random` 后调用要写 `random.randint()`。
- `from random import randint` 后才可以直接写 `randint()`。
- 文件日志通常用 `"a"`，避免覆盖旧内容。
- `datetime.date.today()` 是一层一层调用。


# Day 26：项目结构入门

## 项目结构

```text
day26-project/
├── main.py
├── student_utils.py
├── file_utils.py
└── students.csv
```

## 分工

```text
main.py：主程序入口，负责调用流程
student_utils.py：学生数据处理函数
file_utils.py：文件读写函数
```

## 导入函数

```python
from student_utils import get_students
from file_utils import save_students_csv
```

导入时不写 `.py`。

## main.py 示例

```python
from student_utils import get_students, print_students
from file_utils import save_students_csv, read_students_csv

students = get_students()
save_students_csv(students)

loaded_students = read_students_csv()
print_students(loaded_students)
```

## 要点

- 一个文件不要无限变长，可以拆成多个模块。
- 工具函数放到工具文件里。
- 主程序流程放到 `main.py`。
- `import` 只是导入函数，函数调用才会真正执行。
- 只运行 `main.py`。

## 易错点

- 文件名和 import 名必须一致。
- import 时不要写 `.py`。
- 函数名不能拼错。
- 运行终端要在项目文件夹里。



# Day 27：学习时间记录系统 v1

## 项目结构

```text
day27-study-log/
├── main.py
├── log_utils.py
└── file_utils.py
```

## 核心数据

```python
log = {
    "date": today,
    "content": content,
    "hours": hours
}
```

多个记录：

```python
logs = []
logs.append(log)
```

## 追加写入 CSV

```python
with open("study_log.csv", "a", encoding="utf-8") as file:
    file.write(f"{log['date']},{log['content']},{log['hours']}\n")
```

## 读取 CSV

```python
with open("study_log.csv", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        parts = line.split(",")

        log = {
            "date": parts[0],
            "content": parts[1],
            "hours": float(parts[2])
        }

        logs.append(log)
```

## 输入数字防错

```python
def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Please enter a number.")
```

## 要点

- `main.py` 负责主流程。
- `log_utils.py` 负责学习记录处理。
- `file_utils.py` 负责文件读写。
- `"a"` 是追加写入。
- 有 `return` 的函数，结果要用变量接住。
- CSV 读取后数字仍然要 `float()`。


# Day 28：学生成绩管理系统 v1

## 项目结构

```text
day28-student-system/
├── main.py
├── student_utils.py
└── file_utils.py
```

## 核心流程

```text
输入学生信息
→ 保存 CSV
→ 读取 CSV
→ 打印学生
→ 统计平均分
→ 筛选及格学生
→ 找最高分学生
```

## 重要函数

```python
students = get_students()
save_students(students)

loaded_students = read_students()
print_students(loaded_students)

average_score = get_average_score(loaded_students)
passed_students = get_passed_students(loaded_students)
top_student = get_top_student(loaded_students)
```

## CSV 写入

```python
file.write(f"{student['name']},{student['score']},{student['attendance']}\n")
```

## CSV 读取

```python
parts = line.split(",")

student = {
    "name": parts[0],
    "score": float(parts[1]),
    "attendance": float(parts[2])
}
```

## 找最高分学生

```python
top_student = students[0]

for student in students:
    if student["score"] > top_student["score"]:
        top_student = student
```

## 要点

- `main.py` 负责主流程。
- `student_utils.py` 负责学生数据处理。
- `file_utils.py` 负责文件读写。
- 有 `return` 的函数，结果后面要用就要接住。
- CSV 读取出的数字要用 `float()` 转换。
- `loaded_students` 表示从文件重新读取回来的数据。


# Day 29：菜单版学生成绩管理系统

## 核心升级

Day29 把 Day28 的一次性程序改成菜单式程序。

## 项目结构

```text
day29-student-system/
├── main.py
├── student_utils.py
└── file_utils.py
```

## 菜单循环

```python
while True:
    print("1. Add student")
    print("2. View students")
    print("3. Show summary")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        ...
    elif choice == "4":
        break
```

## 追加写入

```python
with open("students.csv", "a", encoding="utf-8") as file:
    file.write(f"{student['name']},{student['score']},{student['attendance']}\n")
```

## 读取数据

```python
students = read_students()
```

## 查看统计

```python
print_summary(students)
```

## 要点

- `while True` 可以让程序持续运行。
- `break` 用来退出循环。
- 菜单选择用 `if / elif / else`。
- 添加学生用 `"a"` 追加写入。
- 查看和统计前，要先从 CSV 读取数据。
- `main.py` 负责菜单流程。