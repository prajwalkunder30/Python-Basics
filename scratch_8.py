class ATM:
    def __init__(self,abal):

        self.balance1=abal


    def balance(self):
        print("Your current balance is ",self.balance1)
    def withdraw(self):
        print("ENTER AMOUNT TO WITHDRAW")
        awith=int(input("enter w"))
        if self.balance1<awith:
            print("Not possible")
        else:
            print("Withdrawn amount is ",awith)
            print("Remaining amount is ",self.balance1-awith)
    def deposit(self):
        print("ENTER AMOUNT TO DEPOSIT")
        adep=int(input("enter d"))
        print("Deposited amount is ",adep)
        print("Remaining amount is ",self.balance1+adep)
if __name__=='__main__':
    pk=ATM(10000)
    while (True):
        print("WELCOME TO PRAJWAL ATM")
        print("1.BALANCE")
        print("2.WITHDRAW")
        print("3.DEPOSIT")

        print("ENTER A VALID CHOICE")
        userchoice=int(input())
        if userchoice>3:
            print("PLEASE ENTER A VALID CHOICE")
            userchoice=int(input())

        if userchoice==1:
            pk.balance()
        elif userchoice==2:
            pk.withdraw()
        elif userchoice==3:
            pk.deposit()
        else:
            print("not a valid question")
        print("\n Press q to quit and c to continue")
        user_choice2=""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2=input()
            if user_choice2=="q":
                exit()
            elif user_choice2=="c":
                continue



