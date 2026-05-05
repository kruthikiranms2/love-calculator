choice=0
def inpt():
    n = int(input("Enter a number"))
    return n
def factor(n):
    sum=0
    for i in range(1,n):
        if n%i==0: 
            sum= sum + i
    if n==sum:
        print ("value is perfect number")
    else:
        print("not perfect number")
def evod(n):
    if n%2==0:
        print("value is even:")
    else:
        print("value is odd")
choice=int(input("choose number"))
if choice==1:
    n=inpt()
    factor(n)
elif choice==2:
    n=inpt()
    evod(n)
else:
    print("you have chosen a wrong option")