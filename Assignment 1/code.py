books= {
    "101": ["Python Programming", True],
    "102": ["Data Structure", True],
    "103": ["Algorithms", True],
    "104": ["Mathematics", False],
    "107": ["Engineering Chemisrty", True]
}

users = {
    "janvi123": "pass123",
    "kiyan22": "123456",
    "anshika27": "772633",
    "abcxyz": "777777"
}

print("Welcome to the Library System")
new_user = input("Are you a new user? (yes/no): ")

if (new_user == "yes"):
    print("\nPlease Register Yourself")
    username = input("Enter a username: ")
    password = input("Choose a password: ")
    users[username] = password
    print("Registration Successful!")
else:
    print("\nOkay, Lets log in.")
    username = None

while True:
    if (username is None):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

    if (username in users and users[username] == password):
        print("Login successful!\n")
        break
    else:
        print("Wrong Username or password. Try again.\n")
        username = None

print("Here are the books in the Library: ")
for book_id, info in books.items():
    title, available = info
    status = "Available" if available else "Not Available"
    print(f"{book_id}: {title} - {status}")

book_choice = input("\nEnter the Book ID you want to borrow: ")

if book_choice in books:
    if books[book_choice][1] == True:
        books[book_choice][1] = False
        print(f"You borrowed '{books[book_choice][0]}'.")
    else:
        print(f"Sorry, '{books[book_choice][0]}' is not available right now.")
        print("You can wait for the book or ask to reserve it.")
else:
    print("The Book ID does not exist.")

print("\nThank you for using the Library system!")


