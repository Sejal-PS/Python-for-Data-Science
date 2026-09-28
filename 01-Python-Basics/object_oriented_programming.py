# ============================================
# OBJECT-ORIENTED PROGRAMMING (OOP)
# ============================================

# Object-Oriented Programming is a programming
# approach based on classes and objects.


# ============================================
# CLASS AND OBJECT
# ============================================

class Student:

    def display(self):
        print("This is a student.")


student1 = Student()

student1.display()


# ============================================
# CONSTRUCTOR
# ============================================

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Sejal", 22)

student1.display()


# ============================================
# INSTANCE ATTRIBUTES
# ============================================

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employee1 = Employee("Alice", 60000)

print(employee1.name)
print(employee1.salary)


# ============================================
# METHODS
# ============================================

class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b


calculator = Calculator()

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))


# ============================================
# INHERITANCE
# ============================================

class Person:

    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")


class DataScientist(Person):

    def analyze_data(self):
        print("Analyzing data...")


scientist = DataScientist("Sejal")

scientist.introduce()
scientist.analyze_data()


# ============================================
# ENCAPSULATION
# ============================================

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount


account = BankAccount(1000)

account.deposit(500)

print(account.get_balance())


# ============================================
# POLYMORPHISM
# ============================================

class Dog:

    def speak(self):
        print("Dog says: Woof")


class Cat:

    def speak(self):
        print("Cat says: Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak()


# ============================================
# PRACTICAL DATA SCIENCE EXAMPLE
# ============================================

class Dataset:

    def __init__(self, name, rows, columns):
        self.name = name
        self.rows = rows
        self.columns = columns

    def information(self):
        print("Dataset:", self.name)
        print("Rows:", self.rows)
        print("Columns:", self.columns)


dataset = Dataset(
    "Customer Dataset",
    1000,
    12
)

dataset.information()


# ============================================
# PRACTICE
# ============================================

# 1. Create a Student class.
# 2. Add name, age, and marks attributes.
# 3. Create a method to calculate average marks.
# 4. Create an Employee class.
# 5. Practice inheritance using Person and Employee.
# 6. Create a Dataset class with useful methods.
