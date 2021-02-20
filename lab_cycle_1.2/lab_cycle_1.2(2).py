newlist=[]
n=int(input("Enter the number of elements"))
print("Enter the elements")
for i in range(0,n):
    element=int(input())
    if element >100:
        newlist.append("Over")
    else:
        newlist.append(element)
print(newlist)
