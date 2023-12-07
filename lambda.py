#LAMBDA FUNCTION 
s=int(input("enter the side"))
a=lambda s:s*s
print(a(s))
l=int(input("enter the length"))
b=int(input("enter the breadth"))
a=lambda l,b:l*b
print(a(l,b))
b=int(input("enter the breadth"))
h=int(input("enter the height"))
a=lambda b,h:0.5*b*h
print(a(b,h))


