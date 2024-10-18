Logic inside us (Python)

Open repository
More options
Waiting for review
Ratings (22)
Difficulty:
3.0
Usefulness:
3.6
Fun:
3.4
Materials:
3.8
Duration:
 71 min
This is a guided project
To learn the most, try and implement it on your own first, and check the solution only when you feel necessary. However, if you feel completely stuck, feel free to check the step-by-step solution guide
Having grasped the foundational elements of data like strings, integers, dictionaries, and lists, you're now stepping into data processing.

This project delves into algorithm basics, a concept that might seem daunting if you've ever felt averse to mathematics. However, computers handle the complex computations, requiring you to apply logic—often just common sense.

Consider a scenario: if a bicycle tire is flat, how do you decide the amount of air needed? Typically, you'd start pumping and continue until the tire feels adequately inflated for a ride.

This process involves a conditional check (is the tire flat?), initiating a loop (pumping air), and terminating the loop (when the tire is sufficiently inflated). Such conditional checks and loops are fundamental to algorithmic thinking in programming.

Tasks
SHOW ALL CRITERIA
Reuse the array
Copy the array of your two favorite books from a previous project into the data.py file in this project's repository.

The data.py file contains a variable favourite_books with the array from the "Data around us" project.

CRITERIA
Display titles using 'for' loop
Make both book titles visible in the terminal using only one print() inside a for loop.

Both book titles are displayed in the terminal using a for loop and a print() inside it.

CRITERIA
Display authors using 'for' loop
Display the authors of both books in the terminal using a simple for loop.

The authors of both books are displayed in the terminal using a for loop and a print() inside it.

CRITERIA
Check the age of books using 'if'
Check if the first book is newer than 2000 using its is_published_after_2000 key and display the title only if it's True.

The title of the first book is displayed in the terminal if the is_published_after_2000 key is True.

CRITERIA
Check the age of books using 'if/else'
Concatenate the title of the books with a string indicating if the book is newer or older than 2000.

The title of the first book is displayed with appropriate text indicating if it's newer or older than 2000.

The title of the second book is displayed with appropriate text indicating if it's newer or older than 2000.

CRITERIA
Check the age of books switched
Use the not-equal operator (!=) for the same result as the previous task.

The title of the first book is displayed with appropriate text indicating its publication year relative to 2000.

The title of the second book is displayed with appropriate text indicating its publication year relative to 2000.

CRITERIA
Compare the publishing year
Use inequality operators to display the book title with a prefix indicating if it's newer or older than 2000.

The title of the first book is displayed with text indicating if it's newer or older than 2000.

The title of the second book is displayed with text indicating if it's newer or older than 2000.

CRITERIA
Combine the results using loops and conditionals
Combine a loop and a conditional statement to perform the same task as the last time for each book.

The titles of both books are displayed with text indicating their publication year relative to 2000 using a for loop.

The titles of both books are displayed with text indicating their publication year relative to 2000 using a for of loop.

CRITERIA


Hints
In Python, the for loop is commonly used to iterate over each item in a list or any iterable object. Use this loop to go through arrays (lists in Python) and perform actions on each element.

The basic syntax for a for loop in Python is:

for item in iterable:
    # Perform actions with item
Conditional statements in Python use if, elif, and else. These are used to execute different blocks of code based on certain conditions.

The basic syntax for an if statement is:

if condition:
    # Execute this block if condition is true
elif another_condition:
    # Execute this block if the previous condition was false and this condition is true
else:
    # Execute this block if all the above conditions were false
Use comparison operators (==, !=, >, <, >=, <=) within if statements to compare values and decide which block of code to execute.

For checking multiple conditions, you can use logical operators such as and, or, and not.

When you need to check if a certain value exists in a list or not, use the in keyword:

if value in iterable:
    # Execute this block if value is found in iterable
To iterate over the keys and values of a dictionary, use the .items() method in a for loop:

for key, value in dictionary.items():
    # Access key and value
These hints should help you navigate through the tasks using Python's for loops and conditional statements effectively.

