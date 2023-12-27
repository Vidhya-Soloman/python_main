#CO4 
#QN 2

class Time:
 def __init__(self,hour,minute,second):
  self.__hour=hour #__ indicates private
  self.__minute=minute
  self.__second=second
 def __add__(self,other):
  hour=self.__hour+other.__hour
  minute=self.__minute+other.__minute
  second=self.__second+other.__second
  if hour>=24:
    hour=hour%24
  if minute>=60:
    minute%=60
    hour+=1
  if second>=60:
    second%=60
    minute+=1
  return Time(hour,minute,second)
 def display(self):
  print(self.__hour,":",self.__minute,":",self.__second)
t1=Time(12,50,50)
t2=Time(12,25,31)
t=t1+t2
t.display()

