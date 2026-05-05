#1. Check if a number is Even or Odd  
#2. Find the sum of digits of a number  
#3. Reverse a number  
#4. Exit
choice=0
def inpt():
    n= int(input("enter a number:"))
    return(n)
def odeve(n):
    if n%2==0:
        print("is an even number")
    else:
        print("is an odd number")
def sumno(n):
    sum=0
    while n>0:
        r=n%10
        sum=sum+r
        n=n//10
    print(sum)
def rever(n):
    rev=0
    while n>0:
        r=n%10
        rev=rev*10+r
        n=n//10
    print(rev)
def exi(n):
    ty= type(n)
    if ty!=int:
        print("this isn't a number")
choice= input("enter 1 or 2 or 3 or 4")
if choice==1:
    o=inpt()
    odeve(o)
elif choice==2:
    o=inpt()
    sumno(o)
elif choice==3:
    o=inpt()
    rever(o)
else:
    o=inpt()
    exi(o)