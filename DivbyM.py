# 8. print integer 1 to n divisible by m and tell the number which is divisible by m is even or odd

n= int(input("Enter n "))

m=int(input("Enter m "))

print()

for i in range(1,n):

    if (i%m==0):

        print(i,end=" and ")

        if(i%2==0):

            print("Number is Even")

        else:

            print("Number is Odd")
