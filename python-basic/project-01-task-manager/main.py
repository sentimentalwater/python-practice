from task_utils import get_tasks, print_tasks, print_summary, search_subject
from file_utils import write_tasks, read_tasks

while True:
    print("---task system---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Show summary")
    print("4. Search by subject")
    print("5. Exit")

    choose = input("enter number:").strip()

    if choose == "1":
        tasks = get_tasks()
        print_tasks(tasks)
        write_tasks(tasks)
    elif choose == "2":
        tasks = read_tasks()
        print_tasks(tasks)
    elif choose == "3":
        tasks = read_tasks()
        print_summary(tasks)
    elif choose == "4":
        tasks = read_tasks()
        search_subject(tasks)
    elif choose =="5":
        print("Exit")
        break
    else:
        print("no")