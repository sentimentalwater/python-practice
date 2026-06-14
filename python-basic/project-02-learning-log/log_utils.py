def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("enter a number:")

def get_logs():
    logs = []
    date = input("your log date like 2026-06-13:")
    subject = input("your subject:").strip()
    content = input("your content:").strip()
    hours = get_number("learning hours:")

    log = {
        "date": date,
        "subject": subject, 
        "content": content,
        "hours": hours
    }
    logs.append(log)
    return logs

def print_logs(logs):
    for log in logs:
        print("---log---")
        print("date", log["date"])
        print("subject", log["subject"]) 
        print("content", log["content"])
        print("hours", log["hours"])

def get_total(logs):
    total = 0
    for log in logs:
        total = total + log["hours"]

    return total

def get_average(logs):
    total = get_total(logs)
    average = total / len(logs)

    return average

def get_top_hours(logs):
    top = logs[0]
    for log in logs:
        if log["hours"] > top["hours"]:
            top = log

    return top

def search_subject(logs):
    subject = input("search subject:").strip()
    found_logs = []
    for log in logs:
        if log["subject"] == subject:
            found_logs.append(log)

    return found_logs

def search_date(logs):
    date = input("your log date like 2026-06-13:").strip()
    found_logs = []
    for log in logs:
        if log["date"] == date:
            found_logs.append(log)

    return found_logs

def get_summary(logs):
    if len(logs) == 0:
        print("no log")
        return
    else:
        print("--summar--")
        total = get_total(logs)
        print("Total hours:", total)
        average = get_average(logs)
        print("Average hours:", average)
        longest = get_top_hours(logs)
        print("Longest log:", longest)

        count = len(logs)
        print("Log count:", count)
