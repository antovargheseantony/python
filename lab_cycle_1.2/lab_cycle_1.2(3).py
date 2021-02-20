list=["spiderman","ironman","batman"]
count=0
for i in list:
    for j in i:
        if j =='a' or j=='A':
            count=count+1
print("Total number of a is ",count)
