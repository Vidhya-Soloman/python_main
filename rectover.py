#RECTANGLE CLASS WITH OPERATOR OVERLOADING
class Rectangle:
 def __init__(self,l,b): 
  self.l=l;
  self.b=b;
 def area(self):
  return self.l*self.b
 def __lt__(self,other):
  return self.area()<other.area()
obj1=Rectangle(2,3)
obj2=Rectangle(3,4)
print("area 1=",obj1.area())
print("area 2=",obj2.area())
if(obj1<obj2):
 print("Rectangle 2 is greater")
else:
 print("Rectangle 1 is greater")
 