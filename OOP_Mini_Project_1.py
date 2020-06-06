# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# HarryLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input


class Library:
    def __init__(self, list, name):
        self.List = list
        self.name = name
        self.record = {}

    def displayBooks(self):
        print(f"We have following books in our library: {self.name}")
        for book in self.List:
            print(book)

    def lendBook(self, user, book):
        if book not in self.record.keys():
            self.record.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.record[book]}")

    def addBook(self, book):
        self.List.append(book)
        print("Book has been added to the book list")

    def returnBook(self,book):
        self.record.pop(book)

if __name__ == '__main__':
    owner = input("enter the name of the owner : ")
    n = int(input("enter the number of books you have : "))
    booklist = []
    for v in range(n):
        name = input("enter the name of the book you want to add: ")
        booklist.append(name)
    lib_name = input("enter the name of the library : ")
    owner = Library(booklist, lib_name)

    while(True):
        print(f"Welcome to the {owner.name} library. Enter your choice to continue")
        print("1. Display Books")
        print("2. Lend a Book")
        print("3. Add a Book")
        print("4. Return a Book")
        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("Please enter a valid option")
            continue

        else:
            user_choice = int(user_choice)


        if user_choice == 1:
            owner.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend:")
            user = input("Enter your name")
            owner.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add:")
            owner.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return:")
            owner.returnBook(book)

        else:
            print("Not a valid option")

        k= True
        while k:
            g = input("press q for quit and c for continue")
            if g=='q':
                k = False
                exit()
            elif g=='c':
                break
            else:
                print("Please enter valid input")


