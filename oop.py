
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"{self.title} by {self.author}, {self.pages} pages")

    def is_long(self):
        return self.pages > 300

book1 = Book("Ai Engineering", "CiA", 108)
book2 = Book("Python OOP", "CiA", 301)

book1.description()
print("Is book 2 long?", book2.is_long())

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)

    def is_passing(self):
        avg = self.average()
        if avg is None:
            return False
        return avg >= 50

student1 = Student("CiA", 18, [1, 2, 3, 4, 5])
print(f"Average: {student1.average()}")
student1.add_grade(90)
print(f"New average: {student1.average()}")
print(f"Passing?: {student1.is_passing()}")


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def show(self):
        print(f"Owner: {self.owner} and Balance: {self.balance}")

account1 = BankAccount("CiA", 500000000)
account1.deposit(1000000)
account1.withdraw(10000)
account1.withdraw(50000)
account1.show()
