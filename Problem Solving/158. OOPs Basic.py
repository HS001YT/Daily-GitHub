# 🔹 Task – Create and Use a Class
# 🔹 Requirement:
# Create a class named Car
# Constructor should take:
# brand
# model
# year
# Store them as instance variables
# Create a method car_info() that displays all details
# Create a method is_old()
# If year < 2015 → print "Old Car"
# Else → print "Modern Car"
# Create at least one object
# Call both methods

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"\n\nCar Details are:\nCar Brand: {self.brand}\nCar Model: {self.model}\nCar Year: {self.year}")
    
    def is_old(self):
        if self.year < 2015:
            print("Old Car")
        else:
            print("\nCar type: Modern Car")

brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = int(input("Enter car year: "))

# c1 = Car("Mercedes", "G-Wagon", 2020)
c1 = Car(brand, model, year)
c1.car_info()
c1.is_old()