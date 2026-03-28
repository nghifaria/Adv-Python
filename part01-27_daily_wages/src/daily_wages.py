# Write your solution here
hourly_wage = float(input("Hourly wage: "))
hours_worked = float(input("Hours worked: "))
day_of_the_week = input("Day of the week: ")

daily_wages = float(hourly_wage * hours_worked)
if day_of_the_week == "Sunday":
    daily_wages*=2
    
print(f"Daily wages: {daily_wages} euros")
