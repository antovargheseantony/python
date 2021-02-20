def string_R(string):
    firstchar=string[0]
    string1=string[1:].replace(firstchar,"$")
    print(firstchar+string1)
string=input("enter the string:")
string_R(string)

