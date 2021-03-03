data={"red":3,"blue":4,"orange":6}

list1=list(data.items())

list1.sort()
print("Ascending Order ",list1)

list2=list(data.items())
list2.sort(reverse=True)
print("Descending Order ",list2)
