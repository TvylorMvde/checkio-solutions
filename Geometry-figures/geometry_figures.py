from abc import ABC, abstractmethod
from math import pi, sqrt

class Parameters:

    def __init__(self, a):
        self.a = a

    def choose_figure(self, shape):
        self.shape = shape
        
    def perimeter(self):
        return round(self.shape.perimeter(self.a), 2)

    def area(self):
        return round(self.shape.area(self.a), 2)

    def volume(self):
        return round(self.shape.volume(self.a), 2)

    
class Shape(ABC):

    @abstractmethod
    def area(self, a):
        pass

    @abstractmethod
    def perimeter(self, a):
        pass

    def volume(self, a):
        return 0


class Circle(Shape):

    def area(self, a):
        return a ** 2 * pi

    def perimeter(self, a):
        return 2 * pi * a
    

class Triangle(Shape):

    def area(self, a):
        return sqrt(3) / 4 * a ** 2

    def perimeter(self, a):
        return 3 * a


class Square(Shape):
    
    def area(self, a):
        return a ** 2

    def perimeter(self, a):
        return 4 * a


class Pentagon(Shape):
        
    def area(self, a):
        return sqrt(25 + 10 * sqrt(5)) / 4 * a ** 2

    def perimeter(self, a):
        return 5 * a


class Hexagon(Shape):
       
    def area(self, a):
        return (sqrt(3) * 3) / 2 * a ** 2

    def perimeter(self, a):
        return 6 * a


class Cube(Shape):
    
    def area(self, a):
        return 6 * a ** 2

    def perimeter(self, a):
        return 12 * a

    def volume(self, a):
        return a ** 3


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16


    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")




