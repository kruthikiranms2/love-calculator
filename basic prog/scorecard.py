def inpt():
    marks1= float(input("Enter marks for paper one"))
    marks2= float(input("Enter marks for paper two"))
    marks3= float(input("Enter marks for paper three"))
    marks4= float(input("Enter marks for paper four"))
    return(marks1, marks2, marks3, marks4)
def avg(marks1, marks2, marks3, marks4):
    average= (marks1 + marks2+ marks3+marks4)/4
    if average>=90:
        print("Your grade is A1", average)
    elif average>=80 and average<90:
        print("Your grade is A2", average)
    elif average>=70 and average<80:
        print("Your grade is B1", average)
    else: 
        print("Your grade is B2", average)
def output():
    mar1, mar2, mar3, mar4= inpt()
    avg(mar1,mar2,mar3,mar4)
output()