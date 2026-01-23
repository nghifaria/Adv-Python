class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

def sort_by_length(routes: list):
    def length_order(route):
        return route.length
    
    return sorted(routes, key = length_order, reverse=True)

def sort_by_difficulty(routes: list):
    def difficulty_order(route):
        return (route.grade, route.length)

    return sorted(routes, key=difficulty_order, reverse=True)
        