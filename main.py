from graphics import rectangle
from graphics.circle import area as a,perimeter as p
from graphics._3dgraphics import *
l=float(input("Enter the length: "))
b=float(input("Enter the breadth: "))
rectangle.area(l,b)
rectangle.perimeter(l,b)
r=float(input("Enter the radius: "))
a(r)
p(r)
r=float(input("Enter the radius for sphere: "))
sphere.area(r)
sphere.perimeter(r)
l=float(input("Enter the length of cuboid:"))
b=float(input("Enter the breadth of cuboid:"))
h=float(input("Enter the height of cuboid:"))
cuboid.area(l,b,h)
cuboid.perimeter(l,b,h)
