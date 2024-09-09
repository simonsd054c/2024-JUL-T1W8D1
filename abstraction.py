# ABC -> Abstract Base Class
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area():
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    

circle1 = Circle(7)
print(circle1.area())

rect1 = Rectangle(4, 5)
print(rect1.area())