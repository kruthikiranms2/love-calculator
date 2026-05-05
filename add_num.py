count=0
total=0.0
sval=True
while True:
    sval=input("enter a number:")
    if sval!="done":
        fval=float(sval)
        total=total+fval
        count=count+1
    else:
        break
print ("total + count+ avg values are:" ,total,count,(total/count))