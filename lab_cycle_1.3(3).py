print("Enter 3 Numbers : ")
n1=float(input())
n2=float(input())
n3=float(input())

if n1>n2 and n1>n3:
    print(n1,"is large  : ")
elif n2>n1 and n2>n3:
    print(n2," is large: ")
else:
    print(n3,"is large: ")
