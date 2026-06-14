def lu_log():
    content = input("enter your content: ").strip()

    import datetime

    hours = float(input("enter your study hours: "))
    today = datetime.date.today()

    log = {
        "content": content,
        "date": today,
        "hours": hours
    }
    return log

def write_log(log):
    with open ("study_log.txt", "a", encoding="utf-8") as file:
        file.write(f"{log['content']}, {log['date']}, {log['hours']}\n")

log = lu_log()
write_log(log)

print("study log saved")