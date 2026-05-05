num=""
largest = None
smallest = None
while num!="done":
    num = input("Enter a number: ")
    if num>largest:
        largest=num
        print(largest)
    elif num<smallest:
        smallest=num
        print(smallest)
    if num == "done":
        break
    print(num)

print("Maximum", largest)
