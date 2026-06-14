def write_logs(logs):
    with open ("logs.csv", "a", encoding="utf-8") as file:
        for log in logs:
            file.write(f"{log['content']},{log['date']},log['hours']\n")

def read_logs():
    logs = []
    try:
        with open ("logs.csv", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")

                try:
                    log = {
                    "content": parts[0],
                    "date": parts[1],
                    "hours": float(parts[2])
                }
                    logs.append(log)
                except IndexError:
                    print("", line)
                except ValueError:
                    print("", line)

    except FileNotFoundError:
        print("")

    return logs


