#program to create an array accept values and print the sum of all elements
sum=0
list_array= [0] * 5
for i in range(0,5):
    list_array[i]=int(input("enter values"))
    sum=sum+list_array[i]
print(sum)