#The following example converts a de
binaryArray=[]  
#global varia
number=1234
index=0
def binary ( number ) : 
#// user-define
    
    index = 0
 
while ( number != 0 ):
     num= number%10
     binaryArray.append(num)
     number = number / 10; 
     index+=1
print(number)
