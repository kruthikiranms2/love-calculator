choice=0
def inpt():
    number= int(input("enter a number: "))
    return number
def factor(number):
    for i in range (1,number):
        sum=0
        if number%i==0:
            sum=sum+i
    if number==sum:
        print("number is a perfect number")
    else:
        print("number isnt perfect")
def odeve(number):
    if number%2==0:
        print("its even")
    else:
        print("it's odd")
choice= int(input("1 for checking if perfect number or 2 for checking odd or even"))
if choice==1:
    n=inpt()
    factor(n)
elif choice==2:
    n=inpt()
    odeve(n)
else:
    print("wrong choice")