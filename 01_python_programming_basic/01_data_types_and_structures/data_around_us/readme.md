# Data Around us (Python)

## This is a guided project

To learn the most, try and implement it on your own first, and check the solution only when you feel necessary. However, if you feel completely stuck, feel free to check the step-by-step solution guide

Before diving into algorithms, it's crucial to understand what we're coding for: The Data.

Data surrounds us; everything can be considered data: your name, a shopping list, your favorite movies list, or your recent bank transactions.

In this project, you'll learn to write data in a format that both humans and computers can understand. Yes, the code you write will be processed by a machine, which is why it's essential to be meticulous and avoid errors. But don't worry, we're here to help if you get stuck.

Data can be broadly categorized into two parts:

- The first part includes the very foundational building blocks like text and numbers. These are known as types, more precisely, primitive types.
- The second part consists of data structures, such as lists or properties of an object grouped together.

Through this project, you will grasp the practical meaning of data and see what it looks like in code, specifically Python code. This venture into data handling will lay the groundwork for more complex programming tasks ahead.

## Tasks

### [√] Pick two books

_Choose two of your favorite fiction books. Decide which is the first and which is the second. Gather the following information about your books: title, author, year of the first publication, and the names of at least four characters._

Write all of the above information in a text file named **books_info.txt** in your project directory.

1. [√] The **books_info.txt** file contains the following details of two different books: title, author, year of the first publication, and the names of at least four characters.

### [√] Set title

_First, let's get familiar with strings, which are sequences of characters. In Python, we also use variables to store data so that we can reread and reuse them._

Perform the following steps:

- Create a variable named **title** and assign it the title of your favorite book as its value.
- Print the value of **title** using the **print(title)** function.
- Run your script in the terminal to see the output.

1. [√] The script contains a variable named **title** with the title of the chosen book as a string.

2. [√] The script prints the value of **title**.

### [√] Set author

_Create a variable for the author._

Create a variable named **author** and set its value to the author of your favorite book. Print it to the terminal.

1. [√] The script contains a variable named **author** with the author of the chosen book as a string.

2. [√] The script prints the value of **author**.

### [√] Set publication year

_Now, let's work with numbers._

Create a variable named **year** and assign the publication year of your favorite book as its value. Remember to add it as a number. Print it to the terminal.

1. [√] The script contains a variable named **year** with the publication year of the chosen book as a number.

2. [√] The script prints the value of **year**.

### [√] Set millennial flag

_Booleans represent two possible values: True or False. Consider if your book was published after the year 2000._

Create a variable named isNewerThan2000 and set it to **True** if your book was published after 2000, otherwise **False**. Print its value.

1. [√] The script contains a variable named **isNewerThan2000** with a boolean value based on the publication year of the chosen book.

2. [√] The script prints the value of **isNewerThan2000**.

### [√] Set age

_Calculate how old your book is._

Create a variable named **age** and calculate its value by subtracting the **year** variable from the current year. Print the **age**.

1. [√] The script contains a variable named **age** with the age of the book calculated by subtracting its publication year from the current year.

2. [√] The script prints the value of **age**.

### [√] Set characters

_In Python, lists are used to store multiple items in a single variable._

Create a variable named **characters** and assign a list of character names from your book to it. Print the characters.

1. [√] The script contains a variable named **characters** with a list of character names.

2. [√] The list contains names of at least four characters from the book.

3. [√] The script prints the value of **characters**.

### [√] Display specific characters

_You can display only specific characters from the list using indices._

Display the first two characters from the **characters** list.

1. [√] The script prints the value of the first item from the **characters** list.

2. [√] The script prints the value of the second item from the **characters** list.

### [√] Set favorite book

_Group all properties of your book into a single variable using a dictionary._

Create a variable named **favoriteBook** and use a dictionary to store **title**, **author**, **year**, **isNewerThan2000**, **age**, **characters** as its keys with their respective values.

1. [√] The script contains a variable named **favoriteBook** with a dictionary as its value.

2. [√] The dictionary contains keys for **title**, **author**, **year**, **isNewerThan2000**, **age**, **characters** with their respective data.

### [√] Display specific properties

_You can access the value of dictionary keys either using dot notation or bracket notation._

Display the **author** and **year** values of the **favoriteBook** dictionary.

1. [√] The script prints the value of the **author** key from the **favoriteBook** dictionary.

2. [√] The script prints the value of the **year** key from the **favoriteBook** dictionary.

### [√] Display array item through an object

_Access a specific character through the **characters** key of the **favoriteBook** dictionary._

Display the first character from the **characters** list within the **favoriteBook** dictionary.

1. [√] The script prints the first character from the **characters** list within the **favoriteBook** dictionary.

### [√] Set list of books

_Organize multiple book dictionaries within a list._

Create a variable named **favoriteBooks** and assign it a list containing two book dictionaries with the same keys as before.

1. [√] The script contains a variable named **favoriteBooks** with a list of dictionaries as its value.

2. [√] Each dictionary within the list has keys for **title**, **author**, **year**, **isNewerThan2000**, **age**, **characters** with their respective data.

### [√] Display object properties through an array

_Access and display properties of the second book in the **favoriteBooks** list._

Display the **title** of the second book and the first character's name from its **characters** list.

1. [√] The script prints the **title** of the second book in the **favoriteBooks** list.

2. [√] The script prints the first character's name from the **characters** list of the second book.

### [√] Calculate age difference between books

_Calculate and display the age difference between the two books in the **favoriteBooks** list._

The result should not be negative.

1. [√] The age difference between the two books is displayed.

2. [√] The displayed age difference is not a negative number.

### Hints

- Write your code in a Python script file, typically named **data.py**.

- Use **print()** to display outputs instead of **console.log()**.

- Variables in Python don't require the **let**, **var**, or **const** keywords; simply assign values with **=**.

- Python lists (**[]**) serve the same purpose as arrays in JavaScript.

- Python dictionaries (**{}**) are used instead of JavaScript objects for storing key-value pairs.

- When accessing dictionary values, Python allows only the bracket notation (**dict["key"]**) or the dot notation for attributes in custom classes, not for dictionary keys.

- Python does not use semicolons to end statements.

- Be mindful of Python's indentation as it is key to defining blocks of code, especially when defining dictionaries, lists, or control structures.
