# Write your solution here
temp_in_f = int(input("Please type in a temperature (F): "))

celcius = (temp_in_f - 32) * float(5/9)

print(f"{temp_in_f} degrees Fahrenheit equals {celcius} degrees Celsius")

if celcius < 0:
    print("Brr! It's cold in here!")