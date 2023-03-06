expense_categories = {
    'Monday': ('travel expenses', 'lunch', 'entertainment'),
    'Tuesday': ('travel expenses', 'dinner', 'groceries'),
    'Wednesday': ('travel expenses', 'lunch', 'shopping'),
    'Thursday': ('travel expenses', 'dinner', 'entertainment'),
    'Friday': ('travel expenses', 'lunch', 'groceries'),
    'Saturday': ('travel expenses', 'dinner', 'shopping'),
    'Sunday': ('travel expenses', 'lunch', 'entertainment')
}

expense_amounts = [0] * len(expense_categories['Monday'])

for day in expense_categories:
    print(f"Expenses for {day}:")
    for i, category in enumerate(expense_categories[day]):
        expense_amount = float(input(f"  {category}: $"))
        expense_amounts[i] += expense_amount

total_spending = sum(expense_amounts)

print("Amount spent for each category:")
for i, category in enumerate(expense_categories['Monday']):
    print(f"  {category}: ${expense_amounts[i]}")
print(f"Total spending for the week: ${total_spending}")