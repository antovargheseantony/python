a=int(input("enter the number"))
fact=1
if a<=0:
    print("no factorial")
elif a==0:
    print("factotial is 1")
else:
    for i in range(1,a+1):
        fact=fact*i
    print("the factorial of",a,'is',fact)    
