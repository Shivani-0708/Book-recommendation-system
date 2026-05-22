books = {
    "Fantasy": ["Harry Potter", "The Hobbit"],
    "Romance": ["Pride and Prejudice", "Me Before You"],
    "Mystery": ["Sherlock Holmes", "Gone Girl"]
}

genre = input("Enter your favorite genre: ")

if genre in books:
    print("Recommended Books:")
    for book in books[genre]:
        print(book)
else:
    print("Genre not found")