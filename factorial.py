#FUNCTION
#CO2
#QN 1
#FACTORIAL OF A NUMBER
def factorial():
 i=1
 n=int(input("Enter a number:"))
 while(i<n):
  fact=i*n
  i=i+1
 print("Factorial is:",fact)
factorial()