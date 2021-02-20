lista=[1,2,4,5]
listb=[5,7,8,9,10]
length_a=len(lista)
length_b=len(listb)
if(length_a==length_b):
    print("list is empty")
else:
    print("list are not in same length")
total_a=sum(lista)
total_b=sum(listb)
if(total_a==total_b):
    print("sum is equal")
else:
    print("list sum is equal")
output=any(check in listb for check in lista)
print("common value :",output)



