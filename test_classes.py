from classes import *

# Point
print('\nTesting the Point class:\n' + '=' * 25)
a = Point(5, 2)
b = Point(10, 2)
print(f'Point a: (x={a.x}, y={a.y})\nPoint b: (x={b.x}, y={b.y})')

# Line
print('\nTesting the Line class:\n' + '=' * 25)
l = Line(a, b)
print(f'Line Length = {round(l.length(), 4)}')

# Square
print('\nTesting the Square class:\n' + '=' * 25)
s = Square(l)
s_ar = s.area()
s_pr = s.perimeter()
print(f'Square Area = {round(s_ar, 4)}')
print(f'Square Perimeter = {round(s_pr, 4)}')

# Rectangle
print('\nTesting the Rect class:\n' + '=' * 25)
c = Point(5, 5)
w = Line(a, c)
r = Rect(l, w)
r_ar = r.area()
r_pr = r.perimeter()
print(f'Rectangle Area = {round(r_ar, 4)}')
print(f'Rectangle Perimeter = {round(r_pr, 4)}')

# Cube
print('\nTesting the Cube class:\n' + '=' * 25)
cb = Cube(l)
v = cb.volume()
print(f'Cube Volume = {round(v, 4)}')

print('')