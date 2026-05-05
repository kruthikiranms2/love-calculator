def inpt():
    x = int(input("Enter a two digit number:"))
    return x
def process(x):
    digi1= x%10
    digi2= x//10
    sum = digi1+digi2
    multi= digi1*digi2
    if (sum+multi) == x:
        print("Special two digit number", x)
    else:
        print("NOT a Special two digit number", x)
conti="y"
while conti=="y":
    y= inpt()
    process(y)
    conti= input("Do you wish to continue?")
