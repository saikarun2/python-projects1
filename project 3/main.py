class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in the library are: ")
        for book in self.books:
            print(" *" + book)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, this book is either not available or has already been issued to someone else. please wait until the book is available")
            return False
    
    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it.")

class Student:
    def requestBook(self):
        self.book = input("enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("enter the name of the book you want to return: ")
        return self.book


if __name__ == "__main__":
    centraLibrary = Library(["Algorithms", "Django","Clrs","Python Notes"])
    student = Student()
    # centraLibrary.displayAvaliableBooks()
    while(True):
        welcomeMsg = '''\n=== welcome to central Library ===
        please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("thanks for choosing Centeral Library! Have a great day ahead")
            exit()
        else:
            print("Invalid Choice!")
