class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        print(f"This {self.brand} is from {self.year}")

class Car(Vehicle):
    def honk(self):
        print("Beep beep!")

class Motorcycle(Vehicle):
    def wheelie(self):
        print("Doing a wheelie!")

car = Car("Toyota", 2020)
motorcycle = Motorcycle("Volvo", 2008)

car.honk()
motorcycle.wheelie()


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

circle = Circle(2)
rectangle = Rectangle(3, 4)
triangle = Triangle(3, 4)

shapes = [circle, rectangle, triangle]

for shape in shapes:
    print("Shape area:", shape.area())

class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def add_money(self, amount):
        self.__balance += amount
        print(f"{amount} deposited successfully")

    def spend(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!...")
        else:
            self.__balance -= amount
            print(f"{amount} spent!")

    def get_balance(self):
        print(f"Your balance is: {self.__balance}")

wallet = Wallet("CiA", 100000)
wallet.add_money(20000)
wallet.get_balance()
