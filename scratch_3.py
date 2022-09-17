class library:
    def __init__(self,list,name):
        self.bookslist=list
        self.name=name
        self.lendDict={}
    def displayBooks(self):
        print(f"WE HAVE FOLL BOOKS IN LIBRARY :{self.name}")
        for book in self.bookslist:
            print(book)
    def lendBooks(self,user,book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Lender book database is updated.You can take the book now")
        else:
            print(f"Book is already used by{self.lendDict[book]}")
    def addBook(self):
        self.bookslist.append(book)
        print("Book has been added")
    def returnBook(self,book):
        self.lendDict.pop(book)
if __name__=='__main__':
    sak=library(['Python','Maths','C','C++','Java'],"Prajwal")
    while(True):
        print(f"Welcome to the {sak.name} library")
        print("1.Display Books")
        print("2.Lend Books")
        print("3.Add Books")
        print("4.Return Books")
        user_choice=input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter valid option")
            continue
        else:
            user_choice=int(user_choice)

        if user_choice==1:
            sak.displayBooks()
        elif user_choice==2:
            book=input("Enter the name of the book u want to lend")
            user=(input("enter ur name"))
            sak.lendBooks(user,book)
        elif user_choice == 3:
            book = input("Enter the name of the book u want to add")

            sak.addBook()
        elif user_choice == 4:
            book = input("Enter the name of the book u want to return")

            sak.returnBook(book)
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

