# Daily Basic Operations

## 2. 每次开始学习前做什么

日常开始编程学习时，按这个顺序：

1. 打开桌面的 `Visual Studio Code`
2. 打开 `python-practice` 文件夹
3. 确认左侧能看到自己的 `.py` 文件和 `notes/` 文件夹
4. 打开或新建当天要写的 `.py` 文件
5. 打开底部 Terminal
6. 写代码
7. 按 `Ctrl + S` 保存
8. 在 Terminal 中运行代码
9. 修改错误
10. 更新 Markdown 笔记
11. 使用 Git 上传到 GitHub

核心流程：

```text
写代码 → 保存 → 运行 → 修改 → 记笔记 → Git 提交 → GitHub 保存
```

---

## 3. VS Code 基础操作

### 3.1 打开项目文件夹

在 VS Code 中：

```text
File → Open Folder
```

选择：

```text
python-practice
```

VS Code 左侧只显示当前打开的项目文件夹内容，这是正常的。

### 3.2 新建 Python 文件

在 VS Code 左侧文件栏：

1. 右键空白处或文件夹
2. 选择 `New File`
3. 输入文件名，例如：

```text
hello.py
grade_calculator.py
grade_calculator_input.py
```

注意：Python 文件必须以 `.py` 结尾。

### 3.3 保存文件

写完代码后按：

```text
Ctrl + S
```

如果文件标签旁边有小圆点，说明还没有保存。保存后圆点会消失。

---

## 4. Terminal 和 Python 交互模式的区别

### 4.1 普通 Terminal

普通终端通常长这样：

```text
PS C:\Users\A\DCodepython-practice>
```

或者：

```text
C:\Users\A>
```

这里可以输入命令，例如：

```bash
python --version
python hello.py
git status
git add .
git commit -m "message"
git push
```

### 4.2 Python 交互模式

如果看到：

```text
>>>
```

说明已经进入 Python 交互模式。

这里应该输入 Python 代码，例如：

```python
print("hello")
1 + 1
```

不能在 `>>>` 后面输入终端命令，例如：

```bash
python --version
git status
```

否则会报错。

### 4.3 退出 Python 交互模式

如果误入 `>>>`，输入：

```python
exit()
```

然后回车。

或者按：

```text
Ctrl + Z
```

再回车。

退出后应该重新看到：

```text
PS C:\Users\A\DCodepython-practice>
```

---

## 5. 运行 Python 文件

### 5.1 基本命令

在 Terminal 中输入：

```bash
python 文件名.py
```

例如：

```bash
python hello.py
python grade_calculator.py
```

### 5.2 运行前必须保存

固定顺序：

```text
写代码 → Ctrl + S → python 文件名.py
```

如果忘记保存，运行的可能是旧代码。

---

## 10. Markdown 笔记基础操作

Markdown 文件后缀是：

```text
.md
```

常见文件：

```text
00-index.md
python-basics.md
git-basics.md
errors.md
weekly-review.md
daily-basic-operations.md
```

### 10.1 标题

```markdown
# 一级标题
## 二级标题
### 三级标题
```

### 10.2 列表

```markdown
- Python
- Git
- VS Code
```

### 10.3 任务勾选

```markdown
- [x] 安装 Python
- [x] 上传 GitHub
- [ ] 学 input()
- [ ] 学 for loop
```

### 10.4 行内代码

```markdown
`print()` 用来输出内容。
```

### 10.5 代码块

Python 代码：

````markdown
```python
print("Hello, Python")
```
````

终端命令：

````markdown
```bash
python hello.py
git status
```
````

### 10.6 预览 Markdown

在 VS Code 中打开 `.md` 文件后，按：

```text
Ctrl + Shift + V
```

可以预览 Markdown 效果。

---

## 11. 笔记应该写在哪里

写笔记的位置是 VS Code 上方的编辑区，不是下方 Terminal。

### 上方编辑区

用途：

```text
写代码
写 Markdown 笔记
修改文件内容
```

### 下方 Terminal

用途：

```text
运行 Python 文件
执行 Git 命令
查看版本
上传 GitHub
```

不要把 Markdown 内容粘贴到 Terminal 里。

需要记住：

```text
编辑区写 Markdown 源码
预览区看最终效果
Terminal 只输入命令
```

---

## 15. 当前需要记住的核心命令

### Python

```bash
python --version
python 文件名.py
python -c "print('hello python')"
```

### Git

```bash
git status
git add .
git commit -m "message"
git push
```

### Markdown

```text
Ctrl + S：保存
Ctrl + Shift + V：预览 Markdown
```

---

## 16. 当前学习原则

不要依赖聊天记录作为长期知识库。

正确方式是：

```text
聊天负责指导
笔记负责沉淀
代码负责实践
GitHub 负责保存
复盘负责修正
```

有效信息进入 Markdown 笔记后，聊天内容的价值就已经被继承。

日常学习闭环：

```text
提问 / 学习
↓
获得解释和代码
↓
自己手敲、运行、改写
↓
把核心内容写进 Markdown
↓
git add .
git commit -m "message"
git push
↓
GitHub 保存长期成果
```
