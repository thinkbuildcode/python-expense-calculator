income = float(input("Enter your income: "))

food = float(input("Enter your food expenses: "))
rent = float(input("Enter your rent: "))
transport = float(input("Enter your transport expenses: "))

total_expenses = food + rent + transport

remanining_money = income - total_expenses

print("\n --- EXpense Summary ---")
print("Income: ", income)
print("Total Expenses: ", total_expenses)
print("Remaining Money: ", remanining_money)
