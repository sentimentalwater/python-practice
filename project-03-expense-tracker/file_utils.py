def write_expenses(expenses):
    with open ("expenses.csv", "a", encoding="utf-8") as file:
        for expense in expenses:
            file.write(f"{expense['date']},{expense['category']},{expense['item']},{expense['amount']}\n")

def read_expenses():
    expenses = []
    try:
        with open ("expenses.csv", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                parts = line.split(",")

                if line == "":
                    continue

                try:
                    expense = {
                        "date": parts[0],
                        "category": parts[1],
                        "item": parts[2],
                        "amount": float(parts[3])
                    }
                    expenses.append(expense)

                except IndexError:
                    print("", line)
                except ValueError:
                    print("", line)

    except FileNotFoundError:
        print("file not found")

    return expenses