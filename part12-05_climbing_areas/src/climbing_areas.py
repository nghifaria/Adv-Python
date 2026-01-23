class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Correct sort_by_length function (yours was already correct)
def sort_by_length(routes: list):
    def by_length(item: ClimbingRoute):
        return item.length
    return sorted(routes, key=by_length, reverse=True)

# Corrected sort_by_difficulty function
def sort_by_difficulty(routes_list: list): # Renamed parameter for clarity
    def by_difficulty_key(item: ClimbingRoute):
        # Primary sort: grade string (hardest first due to reverse=True)
        # Secondary sort: length (longer first for same grade due to reverse=True)
        return (item.grade, item.length)
    return sorted(routes_list, key=by_difficulty_key, reverse=True)

# Example usage from the problem description:
if __name__ == "__main__":
    r1 = ClimbingRoute("Edge", 38, "6A+")
    r2 = ClimbingRoute("Smooth operator", 11, "7A")
    r3 = ClimbingRoute("Synchro", 14, "8C+")
    r4 = ClimbingRoute("Small steps", 12, "6A+")

    routes = [r1, r2, r3, r4]

    print("Sorted by length:")
    for route in sort_by_length(routes):
        print(route)

    print("\nSorted by difficulty:")
    for route in sort_by_difficulty(routes):
        print(route)

    print("\n--- Test Case 1 from Error ---")
    r1_fail = ClimbingRoute("Small steps", 13, "6A+")
    r2_fail = ClimbingRoute("Edge", 38, "6A+")
    r3_fail = ClimbingRoute("Bukowski", 9, "6A+")
    fail_routes1 = [r1_fail, r2_fail, r3_fail]
    # Expected: Edge, Small steps, Bukowski
    for route in sort_by_difficulty(fail_routes1):
        print(route)

    print("\n--- Test Case 2 from Error ---")
    routes_fail2 = [
        ClimbingRoute("Edge", 38, "6A+"),
        ClimbingRoute("Smooth operator", 9, "7A"),
        ClimbingRoute("Syncro", 14, "8C+"),
        ClimbingRoute("Big cut", 36, "6B"),
        ClimbingRoute("Fruit garden", 8, "6A"),
        ClimbingRoute("No grip", 12 , "6B+"),
        ClimbingRoute("Small steps", 13, "6A+"),
        ClimbingRoute("The Swedish route", 42, "5+")
    ]
    # Expected: Syncro, Smooth operator, No grip, Big cut, Edge, Small steps, Fruit garden, The Swedish route
    for route in sort_by_difficulty(routes_fail2):
        print(route)