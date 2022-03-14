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
         print(f"{book['title']} by {book['author']}")

         #I found this in the "chickens" notes. What does the f do?

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
        # idea being to ask user for a number to select the item (book) to be removed. Oh well...

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
                # tried this on one line but couldn't find the glitch. 
        
                 
                #not ideal removing book by it's title but I'll take it!
        
# my_functions.py

chickens = [
  { "name": "Margaret", "age": 2, "eggs": 0 },
  { "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]


total_eggs = 0

for chicken in chickens:
    total_eggs += chicken["eggs"]
    chicken["eggs"] = 0 # eggs have been collected

print(f"{total_eggs} eggs collected")

    if option == "5":
        print("Updating a book...")
        # TODO - Update a book
        book_ask = input( "What is the title of the book you wish to update?")

        # bed

#  typing test
