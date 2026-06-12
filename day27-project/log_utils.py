def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("please enter a number")

def get_log():
    logs = []
    import datetime
    total_day = get_number("enter your log day:")
    for number in range(1, total_day + 1):
        content = input("what you learn:").strip()
        today = datetime.date.today()
        hours = get_number("your study hours:")

        log = {
            "content": content,
            "date": today,
            "hours": hours
        }
        logs.append(log)
        return logs
    
def print_logs(logs):
    for log in logs:
        print("-log-")
        print("content:", log["content"])
        print("date:", log["date"])
        print("hours:", log["hours"])

def get_total(logs):
    total = 0
    for log in logs:
        total = total + log["hours"]
    return total

def get_average(logs):
    total = get_total(logs)
    average = total / len(logs)
    return average

