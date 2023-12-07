#LONG WORD
def func_long(n):
 max=len(n[0])
 for i in n:
  if max<len(i):
   max=len(i)
 return max
s=input("enter list of words separated by comma: ") 
n=s.split(",")
print("length of longest word is",func_long(n))
func_long(n)