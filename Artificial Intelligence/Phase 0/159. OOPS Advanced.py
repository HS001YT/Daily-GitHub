# 🔹 Task – Inheritance & Method Overriding
# 🔹 Requirement:
# Create a base class named Person
# Constructor should take:
# name
# age
# Create a method display_info() that prints name and age

# Create a derived class named Employee that inherits from Person
# Constructor should take:
# name
# age
# salary
# Store salary as an additional instance variable
# Override the display_info() method
# It should print name, age, and salary

# Create an object of Employee
# Call the overridden method
# 🔹 Additional Requirement (Access Specifiers Concept)

# Inside Person:
# Create:
# one public variable
# one protected variable

# Base Class
class Person:
    def __init__(self, name, age):
        self.name = name                                         # public
        self._age = age                                          # protected  (Single underscore)
        self.__age = age                                         # private  (Double underscore)

    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.__age)

    # Getter method to access private variable
    def get_age(self):
        return self.__age


# Derived Class
class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)                     # Used to acess the bases class constructor
        self.salary = salary

    # Overriding method
    def display_info(self):
        print("Name:", self.name)
        print("Age:", self.get_age())   # Access via getter
        print("Salary:", self.salary)


# Create object
emp = Employee("Rahul", 25, 50000)
emp.display_info()