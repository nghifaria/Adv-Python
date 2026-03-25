# Write your solution here
number = int(input("Please type in a number: "))
n = 1000
if number < n:
    print(f"This number is smaller than {n}")
    n = 100
    if number < n:
        print(f"This number is smaller than {n}")
        n = 10
        if number < n:
            print(f"This number is smaller than {n}")
            

print("Thank you!")    