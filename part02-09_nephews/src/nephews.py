# Write your solution here
donald_duck = ["Huey", "Dewey", "Louie"]
mickey_mouse = ["Morty", "Ferdie"]
name = input("Please type in your name: ")
if name in donald_duck:
    print("I think you might be one of Donald Duck's nephews.")
elif name in mickey_mouse:
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")