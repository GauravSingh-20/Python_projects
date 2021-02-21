string=input()
length=len(string)
i=0
string_E=""
string_O=""
for i in range(0,length):
    if(i%2==0):
        string_E+=string[i]
    else:
        string_O+=string[i]    
    
print(string_E+"  "+string_O) 