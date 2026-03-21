# Write your solution here
student = int(input("How many students on the course? "))

size = int(input("Desired group size? "))

formed = student // size
if (student - size * formed) != 0:
    formed+=1
print(f"Number of groups formed: {formed}")