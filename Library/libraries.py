import random
from datetime import date

students = []


# ? Creating a profile for specific student
def createStudentProfile(name, email):
    id = len(students) + 1
    borrowed = []
    returned = []

    profile = {"id": id, "name": name, "email": email, "borrowed": borrowed,
               "returned": returned, "created": str(date.today())}

    students.append(profile)


# ? Showing all student profiles
def showAllStudentsProfile():
    for student in students:
        print(student)


# ? Taking a book from library by specific student
def borrowedBook(id, bookName):
    for student in students:
        if (student["id"] == id):
            book = {"bookName": bookName, "ISBN": random.getrandbits(
                32), "borrowDate": str(date.today()), "returnedLibrary": False}
            student["borrowed"].append(book)


# ? Return a book to the library
def returnedBook(id, bookName):
    for student in students:
        if (student["id"] == id):
            book = {"bookName": bookName, "returnDate": str(date.today())}
            student["returned"].append(book)
            for book in student["borrowed"]:
                if (book["bookName"] == bookName):
                    book["returnedLibrary"] = True


# ? Show all borrowed books
def showAllBorrowedBooks(id):
    for student in students:
        if (student["id"] == id):
            for books in student["borrowed"]:
                print(books)


# ? Show all returned books
def showAllReturnedBooks(id):
    for student in students:
        if (student["id"] == id):
            for books in student["returned"]:
                print(books)


# ? Creating some student profiles into library
createStudentProfile('Abir Hasan', 'abirhasan@gmail.com')
createStudentProfile('Sakil Mahmud', 'sakilahmmad71@gmail.com')
createStudentProfile('Sumon Kazi', 'sumonkazi@gmail.com')

# ? Show all students profiles
showAllStudentsProfile()


# ? Borrow some books for "Sakil Mahmud" having user id of 2
# ? Borrowed books
borrowedBook(2, "PHP for begginers")
borrowedBook(2, "Master Algorithms")
borrowedBook(2, "Functional programming in JS")
borrowedBook(2, "Making dynamic applications in node.js")
borrowedBook(2, "React.js in modern way")
# ? Returned books
returnedBook(2, "PHP for begginers")
returnedBook(2, "Making dynamic applications in node.js")

# ? Borrow some books for "Abir Hasan" having user id of 1
# ? Borrowed books
borrowedBook(1, "Physics")
borrowedBook(1, "Chemistry")
borrowedBook(1, "Biology")
# ? Returned books
returnedBook(1, "Chemistry")

# ? Borrow some books for "Sumon Kazi" having user id of 3
# ? Borrowed books
borrowedBook(3, "Wordpress form beginner")
borrowedBook(3, "HTML5 and CSS3")
borrowedBook(3, "Modern web development")
borrowedBook(3, "Android studio")
# ? Returned books
returnedBook(3, "HTML5 and CSS3")
returnedBook(3, "Modern web development")
returnedBook(3, "Android studio")

# ? Show all students profiles afted added and returned the books
showAllStudentsProfile()

# ? SHowing the borrowed and returned books of sakil mahmud
showAllBorrowedBooks(2)
showAllReturnedBooks(2)
