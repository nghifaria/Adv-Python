# Write your solution here

eat_times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
avg_week = float(input("How much money do you spend on groceries in a week? "))
daily = float(float(eat_times * price + avg_week) / 7)
weekly = daily * 7
print("Average food expenditure:")
print(f"Daily: {daily} euros")
print(f"Weekly: {weekly} euros")