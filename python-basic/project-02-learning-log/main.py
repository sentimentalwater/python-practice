from log_utils import get_logs, print_logs, search_subject, search_date, get_summary
from file_utils import write_logs, read_logs

while True:
    print("----- Learning Log System -----")
    print("1. Add log")
    print("2. View logs")
    print("3. Show summary")
    print("4. Search by subject")
    print("5. Search by date")
    print("6. Exit")
    
    number = input("enter a number:")

    if number == "1":
        logs = get_logs()
        write_logs(logs)
        print("logs saved to logs.csv")

    elif number == "2":
        logs = read_logs()
        print_logs(logs)

    elif number == "3":
        logs = read_logs()
        get_summary(logs)

    elif number == "4":
        logs = read_logs()
        found_logs = search_subject(logs)

        if len(found_logs) > 0:
            print_logs(found_logs)
        else:
            print("no log")

    elif number == "5":
        logs = read_logs()
        found_logs = search_date(logs)

        if len(found_logs) > 0:
            print_logs(found_logs)
        else:
            print("no log")

    elif number == "6":
        print("over")
        break

    else:
        print("no help")