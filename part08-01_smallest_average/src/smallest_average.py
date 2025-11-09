def average(person: dict) -> float:
    ex_sum = (person["result1"] + person["result2"] + person["result3"]) / 3
    return ex_sum

def smallest_average(person1, person2, person3) -> dict:
    smallest = person1

    if average(person2) < average(smallest):
        smallest = person2

    if average(person3) < average(smallest):
        smallest = person3

    return smallest
