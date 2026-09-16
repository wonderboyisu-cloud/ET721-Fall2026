"""
Isaam Shah
Lab 5: class, objects, methods and attributes
Sep 16, 2026 
"""

print("\n ---------Example 1: class Circle ------------")
class Circle():
    # values that pass to the object of class Circle
    def __init__(self, radius, color):
        self.r = radius
        self.c = color

    # attributes
    pi = 3.14157

    # method
    def circumference(self):
        return 2*self.pi*self.r

# create am instance object of class
c1 = Circle(2, "red")
print(c1.c)
print(c1.circumference())

print("\n ---------Example 1: class Rectangle ------------")
class Rectagle():
    def __init__(self, height, width, color):
        self.h = height
        self.w = width
        self.c = color

    # method to calculate the area 
    def area(self):
        return self.w * self.h

    # method to calculate the perimetere
    def perimeter(self):
        return 2*self.w + 2*self.h

    # method to draw the rectangle
    """
    def drawRectangle(self):
        pit.gca().add_patch(pit.Rectangle(0,0),self.w,self.h,fc=self.c)
        pit.axis("scaled")
        pit.show()
        """
# create instance object of the class
r1 = Rectagle(2, 3, "olive")
print(f"The perimeter of rectangle with height = {r1.h}, width = {r1.w} is {r1.perimeter()}")

print("\n\n ---------EXERCISE ------------")

"""
Car dealership's inventory management system
You are working on  Python program to stimulate a car dealership's inventory management system. The system aims to model cars and their attributes accurately
Task 1: create a class to represent each vehicle. Each car should have attributes for maximum speed and mileage 
Task 2: update the class with the defaut color for all vehicles, "white" 
Task 3: create a class method to assign seating capacity to a vehicle 
Task 4: create a class method to display all the properties of an object class --> "The ___(color) car has ___ seats, with ____ miles and a maximum speed of ___"
Task 5: create two instance objects of the car. One car will have a max speed of 200kph  and mileage of 50,000 kmpl with five seating capacity. The other car has a max speed = 180 kph, mileage = 75,000kmpl, four seating 

"""

class car1():
    def __init__(self, max_speed, miles):
        self.max = max_speed
        self.m = miles

    color = "white"

    def add_seats(self, seats):
        self.s = seats

    def display(self):
        print(f"The {self.color} car has {self.s} seats, with {self.m} miles and a maximum speed of {self.max} kph")
        print("\n")

van = car1(200, 50000)
van.add_seats(5)
van.display()

class car2():
    def __init__(self, max_speed, miles):
        self.max = max_speed
        self.m = miles

    color = "white"

    def add_seats(self, seats):
        self.s = seats

    def display(self):
        print(f"The {self.color} car has {self.s} seats, with {self.m} miles and a maximum speed of {self.max} kph")
        print("\n")

truck = car2(180, 75000)
truck.add_seats(4)
truck.display()