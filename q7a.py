import math

class shape:
    def area(self):
        pass

class Circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

triangle = Triangle(2, 3)
circle = Circle(10)
rectangle = Rectangle(10, 23)

print('Area of the Triangle: ',triangle.area())
print('Area of the Circle: ',circle.area())
print('Area of the Rectangle: ',rectangle.area())