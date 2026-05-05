#Ask for two numbers and print their sum, difference, product, and division

x = int(input("Enter your first number"))
y= int(input("Enter your second number:"))

sum= x+y
print sum
if x>y:
    diff= x-y
    print(diff)
else:
    diff=y-x
    print(diff)