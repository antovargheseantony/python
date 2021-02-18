year1=int(input("Enter the Current Year : "))

year2=int(input("Enter the Final year : "))

for year1 in range(year1,year2+1):
       if(year1%4==0 and year1%100!=0 or year1%400==0):
              print year1


