#CO5 
#QN 1
newfile=open("new.text","w")  #OPEN A NEW FILE "NEW.TXT"(WRITE)
f1=open("text1.txt","r") #READ
f2=open("new.txt","a") #APPEND
t=0
for i in f1:
 t+=1
 if t%2!=0: #ODD LINES
  f2.write(i)