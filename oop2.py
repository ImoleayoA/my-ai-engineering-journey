class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def describe(self):
        print(f"This {self.brand} is from {self.year}")

class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors

    def honk(self):
        print("Beep beep!")

class Motorcycle(Vehicle):
    def __init__(self, brand, year, sidecar):
        super().__init__(brand, year)
        self.sidecar = sidecar

    def wheelie(self):
        print("Doing a wheelie!")

car = Car("Toyota", 2020, 4)
motorcycle = Motorcycle("Volvo", 2008, False)

car.describe()
car.honk()
print("Doors:", car.doors)

motorcycle.describe()
motorcycle.wheelie()
print("Sidecar:", motorcycle.sidecar)


class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

shapes = [Circle(2), Rectangle(3, 4), Triangle(3, 4)]

for shape in shapes:
    print(f"{shape.name} area: {shape.area()}")

class Wallet:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def add_money(self, amount):
        self.__balance += amount
        print(f"{amount} added.  New balance: {self.__balance}")

    def spend(self, amount):
        if amount > self.__balance:
            print("Insufficient funds!...")
        else:
            self.__balance -= amount
            print(f"{amount} spent. New balance: {self.__balance}")

    def get_balance(self):
        print(f"Your balance is: {self.__balance}")

wallet = Wallet("CiA", 100000)
wallet.add_money(20000)
wallet.get_balance()
