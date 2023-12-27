#CO2
#QN 2
#FIBONACCI USING FUNCTION
def func_fib():
 n=int(input("enter the limit: "))
 n1,n2=0,1
 print("fibonacci series is :",n1,n2,end=" ")
 for i in range(2,n):
   n3=n1+n2
   n1=n2
   n2=n3
   print(n3,end=" ")
func_fib()
