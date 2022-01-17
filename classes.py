from math import sqrt
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1 or Point()
        self.p2 = p2 or Point()
    
    def length(self):
        return sqrt((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2)

class Square(Line, Shape):
    def __init__(self, ln: Line):
        self.ln = ln

    def area(self):
        return self.ln.length() ** 2
    
    def perimeter(self):
        return self.ln.length() * 4

class Rect(Shape):
    def __init__(self, l_th, w_th):
        self.l_th = l_th or Line
        self.w_th = w_th or Line

    def area(self):
        return self.l_th.length() * self.w_th.length()
    
    def perimeter(self):
        return (self.l_th.length() + self.w_th.length()) * 2
        
class Cube(Square):
    def __init__(self, ln: Line):
        self.ln = ln

    def volume(self):
        return self.ln.length() ** 3