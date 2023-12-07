#FACTORS OF A NUMBER USING FUNCTION
def func_fact():
 i=1
 n=int(input("enter a number: "))
 while (i<=n):
  if (n%i==0):
   print(i,end=" ")
  i=i+1
func_fact()
