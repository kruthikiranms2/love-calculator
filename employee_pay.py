gsalary=0.0
netsalary=0.0
def inpt():
    name= input("Enter your full name: ")
    bsalary= float(input("Enter your basic salary: "))
    return(name,bsalary)
def gross(bsalary):
    global gsalary
    global netsalary
    hra= .20*bsalary
    ta= .15*bsalary
    ma= .10*bsalary
    gsalary = bsalary+ hra+ ta+ ma
    netsalary= gsalary-(.12*bsalary)
def output():
    name, bsalary= inpt()
    gross(bsalary)
    print(f"Hi {name}")
    print("Your gross salary is:", gsalary)
    print("Your net salary is:", netsalary)
output()
