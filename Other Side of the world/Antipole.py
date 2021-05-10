#latitude=float(input("Enter the latitude value for place"))
#longitude=float(input("Enter the logitude value for place"))

latitude=float("40.09")
longitude=float("-3.47")

antipole_latitude=latitude.__mul__(int("-1"))

if longitude.__le__(float("0")):
    antipole_longitude=longitude.__add__(float("180"))
else:    
    antipole_longitude=longitude.__sub__(float("180"))


print(antipole_latitude)
print(antipole_longitude)