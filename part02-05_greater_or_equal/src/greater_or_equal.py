# Write your solution here
first = int(input("Please type in the first number: "))
second = int(input("Please type in another number: "))
greater = first
if first > second:
    greater = first
    print("The greater number was:", greater)
elif second > first:
    greater = second
    print("The greater number was:", greater)
else:
    print("The numbers are equal!")
    

    