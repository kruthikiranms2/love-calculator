def choice():
    n = int(input("enter a number"))
    return n
def factor(n):
    for i in range (1,n+1):
        if n%i==0:
            print (i)
number = choice()
factor(number)
def multipy(n):
    mult= factor(number)*n
    print (mult)
    return mult
