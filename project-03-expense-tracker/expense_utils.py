def get_number(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("please enter a number:")

def get_expense():
    expenses = []
    date = input("the date like 2026-06-13:").strip()
    category = input("the category:").strip()
    item = input("the item:").strip()
    amount = get_number("the amount:")

    expense = {
        "date": date,
        "category": category,
        "item": item,
        "amount": amount
    }
    expenses.append(expense)

    return expenses

def print_expenses(expenses):
    for expense in expenses:
        print("---expense---")
        print("Date:", expense["date"])
        print("Category:", expense["category"])
        print("Item:", expense["item"])
        print("Amount:", expense["amount"])

def get_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]

    return total

def get_average(expenses):
    total = get_total(expenses)
    average = total / len(expenses)

    return average

def get_expense_number(expenses):
    number = len(expenses)

    return number

def get_top_expense(expenses):
    top = expenses[0]
    for expense in expenses:
        if expense["amount"] > top["amount"]:
            top = expense

    return top

def search_category(expenses):
    category = input("your want category:")
    found_expenses = []
    for expense in expenses:
        if expense["category"] == category:
            found_expenses.append(expense)

    return found_expenses

def search_date(expenses):
    date = input("your want date like 2026-06-13:")
    found_expenses = []
    for expense in expenses:
        if expense["date"] == date:
            found_expenses.append(expense)

    return found_expenses

def get_total_for_different_category(expenses):
    food_total = 0
    transport_total = 0
    study_total = 0
    other_total = 0


    for expense in expenses:
        if expense["category"] == "food":
            food_total = food_total + expense["amount"]
        elif expense["category"] == "transport":
            transport_total = transport_total + expense["amount"]
        elif expense["category"] == "study":
            study_total = study_total + expense["amount"]
        else:
            other_total = other_total + expense["amount"]
           
    print("Food total:", food_total)
    print("Transport total:", transport_total)
    print("Study total:", study_total) 
    print("Other total:", other_total)


def get_summary(expenses):
    if len(expenses) == 0:
        print("No expenses found.")
        return
    else:
        print("---summary---")
        total = get_total(expenses)
        print("Total amount:", total)
        average = get_average(expenses)
        print("Average amount:", average)
        count = get_expense_number(expenses)
        print("Expense count:", count)
        top = get_top_expense(expenses)
        print("Highest expense:", top)

        get_total_for_different_category(expenses)

        
        
        
        
