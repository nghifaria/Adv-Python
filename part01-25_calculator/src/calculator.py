# Write your solution here
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

operation = input("Operation: ")
res = ""
if operation == "add":
    res += f"{num1} + {num2} = {num1+num2}" 
elif operation == "subtract":
    res += f"{num1} - {num2} = {num1-num2}" 
elif operation == "multiply":
    res += f"{num1} * {num2} = {num1*num2}" 
    
print(res)
    
