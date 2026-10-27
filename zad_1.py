class Student:
    def __init__(self, name: str, marks: list):
        self.name = name
        self.marks = marks

    def is_passed(self) -> bool:
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50


# Obiekt 1 - średnia > 50 (zdał)
student_1 = Student("Jan Kowalski", [60, 70, 80])
print(f"Czy {student_1.name} zdał? {student_1.is_passed()}")  # True

# Obiekt 2 - średnia <= 50 (nie zdał)
student_2 = Student("Anna Nowak", [30, 40, 50])
print(f"Czy {student_2.name} zdała? {student_2.is_passed()}")  # False