def inpt():
    n= int(input("Enter a number: "))
    return(n)
def factor(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
def factorial(n):
    mul=1
    for i in range (1,n+1):
        mul=mul*i
    print(mul)
choice= int(input("enter 1 or 2"))
if choice==1:
    number=inpt()
    factor(number)
elif choice==2:
    number=inpt()
    factorial(number)
else:
    print("wrong choice")
        
