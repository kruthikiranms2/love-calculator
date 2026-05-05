#Write a program to print the following series:


#x1 + x2 + x3 + .......... xn terms
#0, 7, 26, 63 .......... p terms
#1/2 + 1/3 + 1/4 + .......... 1/10
#0, 3, 8, 15, 24, ............ to n terms

def inpt():
    y = int (input("Enter a number:"))
    return(y)
def series1(x,n):
    sum=0
    for i in range(1,n+1):
        sum=sum+x**i
    print(sum)
def series2(p):
    for i in range(1,p+1):
       y= ((i**3)-1)
    print(y)
def series3(o):
    sum=0
    for i in range(1,o+1):
        sum=sum+1/i
    print(sum)
def series4(x):
    for i in range(1,x+1):
        y=((i**2)-1)
    print(y)
conti="y"
while conti=="y":
    choice= int(input("Enter 1 or 2 or 3 or 4 : "))
    if choice==1:
        x=inpt()
        series1(x)
    elif choice==2:
        x=inpt()
        series2(x)
    elif choice==3:
        x=inpt()
        series3(x)
    elif choice==4:
        x=inpt()
        series4(x)
    else:
        print("wrong choice")
    conti=input("Do you wish to continue - y ")
