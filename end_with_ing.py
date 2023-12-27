#CO2
#QN 4 
#ADDING ING AT END OR ADDING LY IF ALREADY END WITH ING 

def end_with_ing():
 txt=input("Enter a text: ")
 if len(txt)<3:
   print(txt)
 elif txt[-3:]=="ing":
   print(txt+"ly")
 else:
   print(txt+"ing")
end_with_ing()
