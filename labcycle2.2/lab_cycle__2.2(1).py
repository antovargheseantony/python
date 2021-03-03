
string=input("Enter the string ")

if string.endswith("ing"):
    string=string+"ly"
else:
    string=string+"ing"
print("New String : ",string)
