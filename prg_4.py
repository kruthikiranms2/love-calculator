choice=0
def inpt():
    n = int(input("Enter a number"))
    return n
def factors(n):
    for i in range (1,n+1):
        if n%i==0:
            print(i)
def factorial(n):
    multi=1
    for i in range(1,n+1):#
        multi= multi*i
    print(multi)
#displaying menu
print("1.factors of number")
print("2.factorial of number")
choice= int(input("choose number:"))
#accepting user choice
if choice==1:
    n = inpt()
    factors(n)
elif choice==2:
    n= inpt()
    factorial(n)
else:
    print("you have entered wrong choice")
