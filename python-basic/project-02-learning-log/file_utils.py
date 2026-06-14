def write_logs(logs):
    with open ("logs.csv", "a", encoding="utf-8") as file:
        for log in logs:
            file.write(f"{log['date']},{log['subject']},{log['content']},{log['hours']}\n")

def read_logs():
    logs = []
    try:
        with open ("logs.csv", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")

                if line == "":
                    continue
                try:
                    log = {
                        "date": parts[0],
                        "subject": parts[1],
                        "content": parts[2],
                        "hours": float(parts[3])
                    }
                    logs.append(log)

                except IndexError:
                    print("", line)
                except ValueError:
                    print("", line)
    except FileNotFoundError:
        print("no log")
    return logs
