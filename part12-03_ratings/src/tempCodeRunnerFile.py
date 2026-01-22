class Student:
    """ The class models a single student"""
    def init(self, name: str, id: str, credits: int):
        self.name = name
        self.id = id
        self.credits = credits

    def __str__(self):
        return f"{self.name} ({self.id}), {self.credits} cr."
    

def by_id(item: Student):
    return item.id

def by_credits(item: Student):
    return item.credits

if __name__ == "__main__":
    o1 = Student("Archie", "a123", 220)
    o2 = Student("Marvin", "m321", 210)
    o3 = Student("Anna", "a999", 131)

    students = [o1, o2, o3]

    print("Sort by id:")
    for student in sorted(students, key= by_id):
        print(student)

    print()

    print("Sort by credits:")
    for student in sorted(students, key=by_credits):
        print(student)