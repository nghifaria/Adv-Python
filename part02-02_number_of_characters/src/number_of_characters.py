word = input("Please type in a word: ")
tambahan = "" if len(word) > 1 else "s"
if len(word) > 1:
    print(f"There are {len(word)} letter{tambahan} in the word {word}")
print("Thank you!")