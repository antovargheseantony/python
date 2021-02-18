list=[]
n=int(input("limit : "))

print("Enter the Numbers :")

for i in range(n):
    numbers=int(input())
    list.append(numbers)
print("The Elements are : ",list)

for i in list:
    a=i*i
    print("Square of ",i," = ",a)
