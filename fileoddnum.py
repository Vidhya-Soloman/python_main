#Printing odd numbers in file

new=open("demo.txt","w")
f1=open("text1.txt","r")
f2=open("demo.txt","a")
for i in f1:
 i=int(i)
 if i%2!=0:
  i=str(i)
  f2.write(i)