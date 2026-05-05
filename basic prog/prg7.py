#Write a program to input integer elements into an array of size 20 and perform the following operations:
#Display largest number from the array.
#Display smallest number from the array.
#Display sum of all the elements of the array

ar= [0]*5
for i in range (0,5):
    ar[i]=int(input("Enter number"))
sum=0
large=0
small=99999
for i in range (0,5):
    if ar[i]>large:
        large=ar[i]
    if ar[i]<small:
        small=ar[i]
    sum=sum+ar[i]
print(large, "is largest number")
print(small, "is smallest number")
print(sum, "is sum of number")