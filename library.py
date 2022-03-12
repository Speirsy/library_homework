library = {
    "name": "CodeClan Library",
    "books": [
        {
            "author": "George RR Martin",
            "title": "A Song of Ice and Fire"
        },
        {
            "author": "J R. R. Tolkien",
            "title": "The Hobbit"
        },
        {
            "author": "Paul Barry",
            "title": "Head-First Python"
        },
        {
            "author": "Allen B. Downey",
            "title": "Think Python: How to Think Like a Computer Scientist"
        },
        {
            "author": "Eric Matthes",
            "title": "Python Crash Course"
        }
    ]
}

# Done - Print welcome statement including library name
print("The", library["name"], "bids you a warm welcome!")

quit

option = ""
while option != "q":
    print("Options:")
    print("1 - List all books")
    print("2 - Search for a book by title")
    print("3 - Add a book")
    print("4 - Remove a book")
    print("5 - Update a book")
    print("q - Quit")
    option = input("What would you like to do? \n")

    if option == "1":
        print("Listing all books...")
        # Done - List all books
        # print(library["books"])
        # not very pretty. 
        
    
        for book in library["books"]:
         print(f"{book['author']} by {book['title']}")

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title

        book_ask = input( "What is the title of the book you wish to search?")
        title_scan = library["books"] #how to access "titles"????? is it all in the Brackets?
        for title in title_scan:
            if title == book_ask:
                print("yes")
            else: 
                print("no")


        # print(title_scan)
        # if book_title == library["books"][0]:
        #     print("Book found")
        # else:
        #     print("Book not found")
# You definitely need a loop, you should check each book! 
# The rest of the logic (input/if statement) is perfect, 
# but the if/else should be done in a for loop :slightly_smiling_face:


    if option == "3":
        print("Adding a book...")
        # TODO - Add a book

    if option == "4":
        print("Removing a book...")
        # TODO - Remove a book

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book


