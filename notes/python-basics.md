
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