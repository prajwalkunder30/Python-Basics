class Library():
    def __init__(self, list_of_books, library_name):
        self.book_list = []
        self.list_of_books = list_of_books
        self.library_name = library_name
        self.lend_records = {}
        for i in list_of_books:
            self.book_list.append(i)

    def add_books(self, book):
        self.book_list.append(book)

    def lend_books(self, name, book_name):

        if book_name in self.book_list:
            self.lend_records[book_name] = name
            self.book_list.remove(book_name)
            print("Lended Book are\n")
            print(self.lend_records)
            print("Book Lended Successfully")

        elif len(self.lend_records) < 1 and book_name not in self.book_list:
            print("\nBook is not in the Library\n")

        elif book_name in self.lend_records.keys():
            for key, value in self.lend_records.items():
                if book_name in key:
                    print(f"Book Already lended by {value}")

    def display_books(self):
        print("\nLibrary Books are listed below\n")
        print("\n------------------------------")
        books_list = self.book_list
        print("Books are in Library\n---------------------")
        print(books_list)

        lend_record = self.lend_records
        print("\nWho Lended the book and Books Name\n---------------------")
        print(lend_record)

        print("------------------------------")

    def return_book(self):
        return_book_name = input("Enter Book Name: ").capitalize()
        if return_book_name in self.lend_records.keys():
            self.book_list.append(return_book_name)
            self.lend_records.pop(return_book_name)
        else:
            print("You didn't lended this book")


# def main_list(l):


def main():
    # By deafault variables
    list_books = ['C', 'C++', 'Java', 'python']
    library_name = 'Rashel'
    harry = Library(list_books, library_name)
    print(f"Welecome To {harry.library_name}\n Choose Which things to do")
    while True:
        print(f"(1) Add Books\n(2) Lend Book\n(3) Display Books\n(4) Return Book\n(5) Exit")
        option = int(input("Enter an Integer from 1 to 5: "))
        if option == 1:
            book = input("Enter book name : ").capitalize()
            harry.add_books(book)

        if option == 2:
            name = input("Enter Your Name : ").capitalize()
            print("Books are in Library")
            harry.display_books()
            print("")
            book_name = input("Enter Lend Book Name: ").capitalize()

            harry.lend_books(name, book_name)

        if option == 3:
            harry.display_books()

        if option == 4:
            harry.return_book()
        if option == 5:
            break


