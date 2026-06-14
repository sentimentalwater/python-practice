def write_tasks(tasks):
    with open ("tasks.csv", "a", encoding="utf-8") as file:
        for task in tasks:    
            file.write(f"{task['name']},{task['subject']},{task['planned_hours']},{task['actual_hours']}\n")

def read_tasks():
    tasks = []
    try:
        with open ("tasks.csv", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")
                if line == "":
                    continue
                
                try:
                    task = {
                        "name": parts[0],
                        "subject": parts[1],
                        "planned_hours": float(parts[2]),
                        "actual_hours": float(parts[3])
                    }
                    tasks.append(task)
                
                except IndexError:
                    print("IndexError", line)
                except ValueError:
                    print("ValueError", line)

    except FileNotFoundError:
        print("no file")    
    
    return tasks

