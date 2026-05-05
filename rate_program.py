p= float(input("enter deposit amount:"))
age= float(input("enter age:"))
term= float(input("enter term:"))
if age>=60 and term <=1:
    rate= 8
elif age<60 and term<=1:
    rate=7.5
elif age>=60 and term>1 and term <2:
    rate=9
elif age<60 and term>1 and term <2:
    rate=8
elif age>=60 and term>2 and term <3:
    rate=10
elif age<60 and term>2 and term <3:
    rate=9
elif age>=60 and term>3:
    rate=11
else:
    rate = 10
interest=(p*term*rate)/100
print ("Amt deposited\t" "term\t"  "age\t" "interest\t")
print ("Amt deposited" ,term, age, interest)