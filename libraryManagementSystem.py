class library:
    def __init__(self):
        self.noOfbooks=0
        self.books=[]

    def addbook(self,book):
        self.books.append(book)
        self.noOfbooks=len(self.books)

    def showbooks(self):
        print(f"the library has {self.noOfbooks} books. name of books are :")
        for book in self.books:
            print(book)

    def getbook(self,book):
        self.books.remove(book)

a=library()
while True:
    print("library system\n 1)Add book\t 2)show books\n 3)get book\t 4)exit")
    p = input("your choice (1,2,3,4) : ")
    print("--------------------------------")
    if p=='1':
        book=input("write name of book to add library ")
        a.addbook(book)
        print(f"the {book} book has added to library.")
        print("--------------------------------")
        continue
    elif p=='2':
        a.showbooks()
        print("--------------------------------")
        continue
    elif p=='3':
        s=input("enter the name of book that you want : ")
        a.getbook(s)
        print("--------------------------------")
        continue
    elif p=='4':
        print("thank you..")
        break
    else:
        print("you choose wrong option.")
        print("--------------------------------")
        continue

