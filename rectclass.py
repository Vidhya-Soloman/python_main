class Rectangle:
 def __init__(self,l,b):
  self.l=l
  self.b=b
 def area(self):
   return self.l*self.b
 def perimeter(self):
   return 2*(self.l+self.b)
ob1=Rectangle(2,3)
ob2=Rectangle(4,5)
print("perimetr of rect 1:",ob1.perimeter())
print("perimeter of rect 2:",ob2.perimeter())
print("area of rect 1:",ob1.area())
print("area of rect 2:",ob2.area())
if(ob1.area()<ob2.area()):
 print("rectangle 2 is greater")
else:
 print("rectangle 1 is greater")


 