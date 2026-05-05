def inpt():
    units= int(input("Enter units:"))
    return units
def process(units):
    if units<=100:
        bill= 100*5
    elif units>100 and units <250:
        bill= (100*5)+ (units-100)*10
    else:
        bill= (100*5)+ (150*10)+(units-250)*20
    return bill
def out():
    units=inpt()
    temp= process(units)
    print(temp+85,"is total bill")
out()


