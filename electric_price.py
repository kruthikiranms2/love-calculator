name= input("Enter your name:")
billno= int(input("enter your  bill number:"))
units= int(input("enter total number of units:"))
if units<100:
    billprice= 0
elif units>100 and units<200:
    billprice= (units-100)*2.50
elif units>200 and units<300:
    billprice= 0+ (100*2.5)+ (units-200)*3.50
else:
    billprice = 0 + (100*2.5)+(100*3.50)+ (units-300)*4.5
billprice=billprice+80
print("BILL")
print("Name:",name)
print("bill number:", billno)
print("number of units of electricity used:", units)
print("total electric bill",billprice)

    