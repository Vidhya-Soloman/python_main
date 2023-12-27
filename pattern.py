#CO2
#QN 5
#PATTERN PRINTING USING NESTED FOR LOOP
n=int(input("Enter a limit:"))
for i in range(0,n):
 for j in range(0,i+1):
  print("*",end=" ")
 print(" ")
for i in range(0,n):
 for j in range(0,n-i-1):
  print("*",end=" ")
 print(" ")