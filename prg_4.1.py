def choice():
    n = int(input("enter a number"))
    return n
def factor(n):
    for i in range (1,n+1):
        if n%2==0:
            print (i)