print("TELL ME EITHER YOUR AGE OR YEAR OF BIRTH")
print("1.AGE")
print("2.YEAR OF BIRTH")
userchoice=int(input("ENTER USERCHOICE"))
if userchoice==1:
    age=int(input("enter age"))

    print("your current age is",age)
elif userchoice==2:
    year=int(input("enter year"))
    if year>2019:
        print("You are not born yet")
        exit()
    age=2019-year
    print("your current age is ",age)
else:
    print("enter correct choice")
    exit()
print("Year at which they will turn 100 years is ",2019+100-age)
print("Pick one year I will tell your age then")
y=int(input())
print("Your age will be",y-2019+age)

