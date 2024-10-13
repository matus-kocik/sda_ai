# WRITE YOUR CODE HERE

favorite_books = [
    {
        "title": "The Witcher",
        "author": "Andrzej Sapkowski",
        "year": 2001,
        "is_published_after_2000": True,
        "characters": ["Geralt, Yennefer, Ciri, Triss, Dandelion"],
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "year": 1937,
        "is_published_after_2000": False,
        "characters": ["Bilbo, Gandalf, Thorin, Smaug"],
    },
]

for book in favorite_books:
    print(book["title"])

# list comprehension:

[print(book["title"]) for book in favorite_books]

print("*" * 50)

for book in favorite_books:
    print(book["author"])

print("*" * 50)

if (
    favorite_books[0]["is_published_after_2000"] == True
):  # True tu nieje potrebne ale pre cvicenie ok...
    print(favorite_books[0]["title"])

print("*" * 50)

if favorite_books[0]["is_published_after_2000"]:
    print(f"{favorite_books[0]["title"]} is newer than 2000")
else:
    print(f"{favorite_books[0]["title"]} is older than 2000")

if favorite_books[1]["is_published_after_2000"]:
    print(f"{favorite_books[1]["title"]} is newer than 2000")
else:
    print(f"{favorite_books[1]["title"]} is older than 2000")

# for loop:
for book in favorite_books:
    if book["is_published_after_2000"]:
        print(f"{book['title']} is newer than 2000")
    else:
        print(f"{book["title"]} is older than 2000")

print("*" * 50)

for book in favorite_books:
    if book["is_published_after_2000"] != False:
        print(
            f"{book['title']} is newer than 2000 and published year is {book["year"]}"
        )
    else:
        print(
            f"{book['title']} is older than 2000 and published year is {book["year"]}"
        )

# list comprehension and ternary operator:

[
    (
        print(
            f"{book['title']} is newer than 2000 and published year is {book["year"]}"
        )
        if book["is_published_after_2000"]
        else print(
            f"{book['title']} is older than 2000 and published year is {book["year"]}"
        )
    )
    for book in favorite_books
]

print("*" * 50)


[
    (
        print(f"{book["title"]} is newer than 2000")
        if book["year"] > 2000
        else print(f"{book["title"]} is older than 2000")
    )
    for book in favorite_books
]

print("*" * 50)
# only for try items() method
for book in favorite_books:
    for key, value in book.items():
        print(f"This is key: {key}, and this is value: {value}")
