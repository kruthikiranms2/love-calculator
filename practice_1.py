for i in range (0,5):
    age= int(input("enter age:"))
    gender = input(" enter M or F")
    days_worked = float(input("enter number of days worked"))
    if age >= 18 and age<30 and gender == "M":
        wages= days_worked * 500
        print("men's wages under 30", wages)
    elif age >= 18 and age<30 and gender == "":
        wages= days_worked * 520
        print("women's wages under 30", wages)
    elif age > 30 and age<=40 and gender == "M":
        wages= days_worked * 700
        print("men's wages over 30", wages)
    elif age > 30 and age<=40 and gender == "F":
        wages= days_worked * 720
        print("women's wages over 30", wages)
