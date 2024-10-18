Reusable functions (Python)

Open repository
More options
Waiting for review
Ratings (7)
Difficulty:
3.9
Usefulness:
4.4
Fun:
4.0
Materials:
4.2
Duration:
 84 min
Time to get a better understanding of functions and how to use them. For this, you will use your previous datasets again, and create reusable functions which work the same way on different data.

Tasks
SHOW ALL CRITERIA
Reuse the arrays
Copy the following data into the data.py file in your project repository:

The favorite_books list from the Data Around Us project.
The fav_movies list from the My Top 4 Movies project.
The best_selling_albums list from the Best Selling Albums project.
The data.py file contains a favorite_books variable. The value is the list from the "Data Around Us" project.

The data.py file contains a fav_movies variable. The value is the list from the "My Top 4 Movies" project.

The data.py file contains a best_selling_albums variable. The value is the list from the "Best Selling Albums" project.

CRITERIA
Show the average age of objects
Create a function named average_age. This function should take two parameters: an array of objects and a number representing the current year. Call this function three times, each time with a different dataset (favorite_books, fav_movies, best_selling_albums) as the first argument and the current year as the second. The function should calculate and return the average age of the objects in the array. Remember to print the results.

An average_age function exists and calculates the average age based on the year keys of the objects in any given list.

The function is called three times with the three different lists (favorite_books, fav_movies, best_selling_albums) as the first argument and the current year as the second.

The results of the three average_age function calls are displayed in the terminal when the data.py file is run.

CRITERIA
Show the average of different properties
Create a function named average. This function should take two parameters: a list of objects and a string indicating a key. If the key exists in the objects, iterate through the list to calculate the average of that key's values. Test the function by calling it on the best_selling_albums list with the sale key and then on the fav_movies list with the rating key. Print the results.

An average function exists and calculates the average of a specified key's values in any list of objects, provided the value is numerical.

The function is called twice: first with fav_movies and the key rating, and second with best_selling_albums and the key sale.

The results of the average function calls are displayed in the terminal when the data.py file is run.

CRITERIA
Show the latest and the oldest objects
Create a latest_or_oldest function with two parameters: a list of objects and a boolean. Depending on the boolean, the function should return the title of either the latest or the oldest object in the list, based on the year key. Call this function three times with different arrays (favorite_books, fav_movies, best_selling_albums) as the first argument and a boolean as the second. Print the results.

A latest_or_oldest function exists that returns the title of either the latest or the oldest object in any given list that contains a year key.

The function is called three times with different lists (favorite_books, fav_movies, best_selling_albums) as the first argument and a boolean indicating whether to return the latest (true) or oldest (false) object's title.

The results of the latest_or_oldest function calls are displayed in the terminal when the data.py file is run.

CRITERIA


Hints
You can visit the previous projects any time to check your solutions.

