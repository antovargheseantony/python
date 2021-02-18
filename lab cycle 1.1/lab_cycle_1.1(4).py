list1=[]
vowels=['a','e','i','o','u']
s=input("enter the string:")
for i in vowels:
    if(i in s):
        list1.append(i)
print("vowels present in string",list1)
