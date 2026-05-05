x = int(input("Enter a 2 digit number:"))

digi1= x%10
digi2= x//10
sum = digi1+digi2
multi= digi1*digi2
if (sum+multi) == x:
    print("Special two digit number", x)
else:
    print("NOT a Special two digit number", x)