from expense_utils import get_expense, print_expenses, search_category, search_date, get_summary
from file_utils import write_expenses, read_expenses

while True:
    print("-- Expense Tracker --")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Show summary")
    print("4. Search by category")
    print("5. Search by date")
    print("6. Exit")

    choose = input("choose a number:").strip()

    if choose == "1":
        expenses = get_expense()
        write_expenses(expenses)
        print("expenses saved to expenses.csv")

    elif choose == "2":
        expenses = read_expenses()
        print_expenses(expenses)

    elif choose == "3":
        expenses = read_expenses()
        get_summary(expenses)

    elif choose == "4":
        expenses = read_expenses()
        found_expenses = search_category(expenses)
        if len(found_expenses) == 0:
            print("no found")
        else:
            print_expenses(found_expenses)

    elif choose == "5":
        expenses = read_expenses()
        found_expenses = search_date(expenses)
        if len(found_expenses) == 0:
            print("no found")
        else:
            print_expenses(found_expenses)    

    elif choose == "6":
        print("bye")
        break

    else:
        print("please enter a number")
