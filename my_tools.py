def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def circle_area(radius):
    return 3.14159 * radius * radius

MY_NAME = "CiA"


if __name__ == "__main__":
    print("Testing my_tools...")
    print(add(2, 3))
    print(subtract(10, 4))
    print(multiply(5, 2))
    print(is_even(8))
    print(circle_area(2))
