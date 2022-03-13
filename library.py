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
               
                # print(library["books"])
                # not very pretty. 
        
    
        for book in library["books"]:
         print(f"{book['author']} by {book['title']}")

    if option == "2":
        print("Searching for a book by title...")
        # TODO - Search for a book by title

        book_ask = input( "What is the title of the book you wish to search?")
        books = library["books"]
        for book in books:
            if book["title"] == book_ask:
                print("Yes we have the book")
            else: 
                print("Not in library")


    
# You definitely need a loop, you should check each book! 
# The rest of the logic (input/if statement) is perfect, 
# but the if/else should be done in a for loop :slightly_smiling_face:


    if option == "3":
        print("Adding a book...")
        # TODO - Add a book
        author_in = input( "Who is the author of the book you wish to add?")
        title_in = input( "What is the title of the book you wish to add?")
        library["books"].append({"author":author_in, "title":title_in})
        #It works!!! How / Where is the added data being stored?


    if option == "4":
        print("Removing a book...") 
        # TODO - Remove a book
        # print books list adding index number. Can't figure this out. 
        # idea being to ask user for a number to select the item (book) to be removed.
        for book in library["books"]:
         print(f"{book['title']} by {book['author']}")
        
        # borrow loop from option 2 and 
        book_ask = input( "What is the title of the book you wish to remove?")
        books = library["books"] 
        for book in books:
            if book["title"] == book_ask:
                books.remove(book)
                print(book["title"]) 
                print("by")
                print(book["author"])
                print("is removed")
                
        
            # print(f"{book['title']} by {book['author']} is removed")        
                #not ideal removing book by it's title but I'll take it!

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
        book_ask = input( "What is the title of the book you wish to update?")


