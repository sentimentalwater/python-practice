
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