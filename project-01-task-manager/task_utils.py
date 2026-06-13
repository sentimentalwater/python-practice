def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("enter a number:")

def get_tasks():
    tasks = []
    task_number = int(get_number("your task number:"))
    for number in range(1, task_number + 1):
        task_name = input(f"your task {number} name:").strip()
        subject = input(f"your subject in task {number}:").strip()
        planned_hours = get_number(f"your planned hours in task {number}:")
        actual_hours = get_number(f"youe actual hours in task {number}:")
        task = {
            "name": task_name,
            "subject": subject,
            "planned_hours": planned_hours,
            "actual_hours": actual_hours
        }
        tasks.append(task)
    return tasks

def print_tasks(tasks):
    for task in tasks:
        print("--task--")
        print("name:", task["name"])
        print("subject:", task["subject"])
        print("planned hours:", task["planned_hours"])
        print("actual hours:", task["actual_hours"])

def get_total_planned(tasks):
    total = 0
    for task in tasks:
        total = total + task["planned_hours"]
    return total

def get_total_actual(tasks):
    total = 0
    for task in tasks:
        total = total + task["actual_hours"]
    return total

def get_actual_average(tasks):
    total = get_total_actual(tasks)
    actual_average = total / len(tasks)
    return actual_average

def get_completed_tasks(tasks):
    completed_tasks = []
    for task in tasks:
        if task["actual_hours"] >= task["planned_hours"]:
            completed_tasks.append(task)
    return completed_tasks

def get_uncompleted_tasks(tasks):
    uncompleted_tasks = []
    for task in tasks:
        if task["actual_hours"] < task["planned_hours"]:
            uncompleted_tasks.append(task)
    return uncompleted_tasks

def get_top_actual(tasks):
    top_actual = tasks[0]
    for task in tasks:
        if task["actual_hours"] >= top_actual["actual_hours"]:
            top_actual = task
    return top_actual

def print_summary(tasks):
    if len(tasks) > 0:
        print("---summary---")
        
        total_planned = get_total_planned(tasks)
        print("total planned:", total_planned)
        
        total_actual = get_total_actual(tasks)
        print("total actual:", total_actual)

        actual_average = get_actual_average(tasks)
        print("actual average:", actual_average)

        completed_tasks = get_completed_tasks(tasks)
        print("completed tasks:", completed_tasks)

        uncompleted_tasks = get_uncompleted_tasks(tasks)
        print("uncompleted tasks:", uncompleted_tasks)

        top_actual = get_top_actual(tasks)
        print("top actual:", top_actual)

    else:
        print("no task found")

def search_subject(tasks):
    subject_name = input("your search subject:").strip()
    matched_tasks = []
    for task in tasks:
        if task["subject"] == subject_name:
            matched_tasks.append(task)

    if len(matched_tasks) > 0:
        print_tasks(matched_tasks)  
    else:
        print("no task found")
