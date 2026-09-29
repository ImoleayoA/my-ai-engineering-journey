class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"Title by {self.author}, X {self.pages}")

    def is_long(self):
        if self.pages > 300:
            print(True)
        else:
            print(False)

book1 = Book("Ai Engineering", "CiA", 108)
book2 = Book("Python OOP", "CiA", 301)

book1.description()
book2.is_long()

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        if not self.grades:
            print("No grades")
        print(sum(self.grades) / len(self.grades))

    def add_grade(self, grade):
        self.grades += grade

    def is_passing(self):
        if average() >= 50:
            print(True)
        else:
            print(False)

student1 = Student("CiA", 18, [1, 2, 3, 4, 5])
student1.average()
