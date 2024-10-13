# The following line is an example of how you can add a string (aka text) value to a variable.
exampleVariable = "This is a string added to the variable named exampleVariable"

"""
Explanation:

[variable name] [equal sign] [value]

[variable name]: `exampleVariable`
You can give almost any name to a variable, but be careful with two things:
1. Don't use special characters in it.
2. Use the "snake_case" form where words are separated by underscores, 
   and all letters are in lowercase (e.g., this_is_a_snake_case_text).
   Alternatively, Python also allows "camelCase" like JavaScript, but "snake_case" is more common in Python for variable names.
It is recommended to use the English language throughout your code, especially (but not exclusively) for variable names.

[equal sign]: `=`
Remember, the equal sign between the variable name and the value is crucial.
This serves as the "assignment operator" which assigns the value to the variable.

[value]: `"This is a string added to the variable named exampleVariable"`
The value is the piece of data you want to assign (save) to the variable for later use.

In Python, there's no need for a semicolon at the end of the line.
"""

# The following line is just an example of how you can print text to the console using `print()`.
# You have to write a value or a variable name inside the parentheses.
print(exampleVariable)
print("*" * 20)

# WRITE YOUR CODE HERE

title = "The Witcher"

print(title)
print("*" * 20)

author = "Andrzej Sapkowski"

print(author)
print("*" * 20)

year = 1993

print(year)
print("*" * 20)

isNewerThan2000 = False

print(isNewerThan2000)
print("*" * 20)

age = 2024 - year

print(age)
print("*" * 20)

characters = ["Geralt", "Yennefer", "Ciri", "Triss", "Jaskier"]

print(characters)
print(characters[0])
print(characters[1])
print("*" * 20)

favoriteBook = {
   "title": "The Witcher",
   "author": "Andrzej Sapkowski",
   "year": 1993,
   "isNewerThan2000": False,
   "characters": ["Geralt", "Yennefer", "Ciri", "Triss", "Jaskier"],
}

print(favoriteBook)
print(favoriteBook["author"])
print(favoriteBook["year"])
print(favoriteBook["characters"][0])
print("*" * 20)

favoriteBooks = [
{
   "title": "The Witcher",
   "author": "Andrzej Sapkowski",
   "year": 1993,
   "isNewerThan2000": False,
   "characters": ["Geralt", "Yennefer", "Ciri", "Triss", "Jaskier"],
},
{
   "title": "The Hobbit",
   "author": "J.R.R. Tolkien",
   "year": 1937,
   "isNewerThan2000": False,
   "characters": ["Bilbo", "Gandalf", "Thorin", "Smaug"],
},
]

print(favoriteBooks[1]["title"])
print(favoriteBooks[1]["characters"][0])
print("*" * 20)


print(abs(favoriteBooks[0]["year"] - favoriteBooks[1]["year"]))