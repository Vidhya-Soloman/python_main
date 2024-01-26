#GCD OF TWO NUMBERS 
#WITHOUT MATH FUNCTION

a=int(input("Enter a number"))
b=int(input("Enter a number"))
gcd=1
for i in range(1,b+1):
 if(a%i==0 and b%i==0):
   gcd=i
print(gcd)