def inpt():
    numb= int(input("enter number:"))
    return numb
def process(numb):
    for i in range(1,numb+1):
        if numb%i==0:
            print(i)
numb=inpt()
process(numb)