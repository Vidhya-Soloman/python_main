#CO4
#QN 3

class Publisher:
 def __init__(self,name):
   self.name=name

 def display(self):  #METHOD OVERRIDING
   print("Name of the book: ",self.name)

class Book(Publisher):
  def __init__(self,name,title,author):
    super().__init__(name)
    self.title=title
    self.author=author

  def display(self): #METHOD OVERRIDING
    print("Title of the book: ",self.title)
    print("Author of the book: ",self.author)

class Python(Book):
 def __init__(self,name,title,author,price,pages):
    super().__init__(name,title,author)
    self.price=price
    self.pages=pages

 def display(self): #METHOD OVERRIDING
    print("Name of the book: ",self.name)
    print("Title of the book: ",self.title)
    print("Author of the book: ",self.author)
    print("Price of the book: ",self.price,"Rs")
    print("No of pages of the book: ",self.pages)
p1=Python("Python","Python Pocket Reference","Mark Lutz",447,1024)
p1.display()

 

  