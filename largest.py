def inp():
    a= int(input("Enter any number:"))
    b= int(input("Enter any number:"))
    c= int(input("Enter any number:"))
    return a,b,c
def process(a,b,c):
    if a>b and a>c:
        lar=a
    elif b>a and b>c:
        lar=b
    else:
        lar=c
    return lar
def out():
    a,b,c= inp()
    temp= process(a,b,c)
    print(temp)
out()
    