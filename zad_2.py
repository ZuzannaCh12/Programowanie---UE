class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self) -> str:
        return f"Biblioteka w {self.city}, ul. {self.street} ({self.zip_code})"


class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self) -> str:
        return f"Pracownik: {self.first_name} {self.last_name}"


class Student:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f"Student: {self.name} {self.surname}"


class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self) -> str:
        return f"Książka: '{self.author_name} {self.author_surname}' ({self.number_of_pages} str.) z [{self.library}]"


class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books  # lista obiektów klasy Book
        self.order_date = order_date

    def __str__(self) -> str:
        books_str = "\n  - ".join([str(book) for book in self.books])
        return (f"Zamówienie z dnia {self.order_date}:\n"
                f" Obsługujący: {self.employee}\n"
                f" Zamawiający: {self.student}\n"
                f" Zamówione książki:\n  - {books_str}\n")


# 1. Tworzenie 2 bibliotek
lib1 = Library("Katowice", "Bankowa 12", "40-007", "8:00-19:00", "321234567")
lib2 = Library("Kraków", "Grodzka 5", "31-001", "9:00-17:00", "129876543")

# 2. Tworzenie 5 książek
b1 = Book(lib1, "2010", "Adam", "Mickiewicz", 350)
b2 = Book(lib1, "1896", "Henryk", "Sienkiewicz", 550)
b3 = Book(lib2, "1954", "J.R.R.", "Tolkien", 420)
b4 = Book(lib2, "1949", "George", "Orwell", 320)
b5 = Book(lib2, "1961", "Stanisław", "Lem", 280)

# 3. Tworzenie 3 pracowników
emp1 = Employee("Jan", "Kowalski", "2020-01-15", "1990-05-12", "Katowice", "Mariacka 2", "40-010", "500100200")
emp2 = Employee("Anna", "Nowak", "2021-03-01", "1995-08-20", "Katowice", "Stawowa 5", "40-018", "500200300")
emp3 = Employee("Piotr", "Wiśniewski", "2019-11-10", "1988-12-01", "Kraków", "Długa 10", "31-140", "500300400")

# 4. Tworzenie 3 studentów
st1 = Student("Zuzanna", "Chmielewska")
st2 = Student("Michał", "Krawczyk")
st3 = Student("Katarzyna", "Zielińska")

# 5. Tworzenie 2 zamówień
ord1 = Order(emp1, st1, [b1, b2], "2024-10-15")
ord2 = Order(emp3, st2, [b3, b4, b5], "2024-10-16")

# Wyświetlenie obu zamówień
print(ord1)
print(ord2)