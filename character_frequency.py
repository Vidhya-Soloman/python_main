#CO2
#QN 3
#COUNTING CHARACTERS USING FUNCTION
def count_character():
 txt=input("Enter a text: ")
 freq={}
 for i in txt:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
 print("counting each character:",freq)
count_character()
