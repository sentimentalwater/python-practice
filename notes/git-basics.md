## 1. 日常修改后如何上传到 GitHub

当我新增、修改或删除文件后，如果想同步到 GitHub，使用下面四步：

```bash
git status
git add .
git commit -m "说明这次改了什么"
git push
```

### 1. 查看当前状态

```bash
git status
```

作用：查看当前有哪些文件被新增、修改或删除。

常见提示：

* `modified`：文件被修改
* `new file`：新增文件
* `deleted`：文件被删除
* `nothing to commit, working tree clean`：当前没有需要提交的修改

### 2. 添加所有修改

```bash
git add .
```

作用：把当前文件夹中的所有修改加入暂存区，包括新增、修改、删除的文件。

### 3. 提交一次版本记录

```bash
git commit -m "说明这次改了什么"
```

作用：正式记录这次修改。

示例：

```bash
git commit -m "add markdown notes"
git commit -m "remove unnecessary file"
git commit -m "update git basics notes"
```

### 4. 上传到 GitHub

```bash
git push
```

作用：把本地提交上传到 GitHub。

### 常用完整流程

```bash
git status
git add .
git commit -m "update notes"
git push
```

### 需要理解

* `git status`：先检查发生了什么变化
* `git add .`：把变化加入准备提交的区域
* `git commit`：在本地保存一次版本记录
* `git push`：把本地记录上传到 GitHub

### 注意

如果只是修改了 `.md` 笔记，要先按 `Ctrl + S` 保存，再执行 Git 命令。

如果是删除文件，不需要 `Ctrl + S`，但仍然需要执行：

```bash
git add .
git commit -m "remove unnecessary file"
git push
```

这样 GitHub 上才会同步删除。
