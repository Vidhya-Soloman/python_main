from graphics import circle
#from graphics._3dgGraphics import cuboid
from graphics import rectangle
from graphics._3dgraphics import *
l=float(input("Enter the length: "))
b=float(input("Enter the breadth: "))
rectangle.area(l,b)
rectangle.perimeter(l,b)
r=float(input("Enter the radius: "))
circle.area(r)
circle.perimeter(r)
r=float(input("Enter the radius for sphere: "))
sphere.area(r)
sphere.perimeter(r)
l=float(input("Enter the length o cuboid:"))
b=float(input("Enter the breadth of cuboid:"))
h=float(input("Enter the length of cuboid:"))
cuboid.area(l,b,h)
cuboid.perimeter(l,b,h)
