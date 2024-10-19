# Missing heroes (Python)

Once again, same familiar data, familiar tasks, but this time using loops and conditional statements.

## Tasks

### [√] Missing Martin

Martin Scorsese is missing from the data of his movies. Wherever there is an empty string as the value of the 'director' key, add Martin Scorsese.

1. [√] There are no objects in the movies list with an empty string as the value of the 'director' key.

2. [√] Martin Scorsese appears four times as director.

### [√] Correct wrong release years

The release year is incorrect for five films. Each is one thousand or two thousand years less than it should be. Correct the years by adding 1000 or 2000 to them.

1. [√] The 'year' key value for every movie is greater than 1900.

### [√] Leonardo is mixed up

Instead of Leonardo DiCaprio, Leonardo da Vinci is listed among the actors. Correct this mistake.

1. [√] Leonardo da Vinci is not listed as an actor in any of the movies.

2. [√] Leonardo DiCaprio is listed as an actor in six movies.

### [√] Add drama

The 'Drama' genre is missing from the genre lists of several movies. Wherever there is an empty string as an item of the 'genres' list, add the 'Drama' genre.

1. [√] There are no empty strings in the genres lists.

2. [√] The genre 'Drama' appears 98 times in the genres lists of the movies.

### [√] How many actors are in the list?

Count how many actors are in the list. Store the result in the 'allTheActors' variable. First, count all names without worrying about duplicate names. Then, if you feel up for the challenge (optional), try filtering out duplicates!

1. [√] There is an 'allTheActors' variable the value of which is the number of all the actors in the list.


## General requirements

- Modifications are made in a separate Python script, utilizing loops, conditionals (if/else), and accessing data structures with Python's syntax.

## Hints

For this project, you'll be working in a separate Python script to modify a provided list of movies. Remember, do not alter the original data structure directly in the **data.py** file. Instead, use the **corrections.py** file for your changes. Here are some Python-specific strategies:

- To add "Martin Scorsese" where the director's name is missing, iterate over the movies list and check the 'director' key in each dictionary.

- To correct release years, use a loop and conditionally check and modify the 'year' key.

- Replace "Leonardo da Vinci" with "Leonardo DiCaprio" by checking the 'actors' list within each movie dictionary.

- For missing 'Drama' genres, iterate through each movie's 'genres' list and add "Drama" where necessary.

- To count actors, consider creating a set to automatically filter out duplicates if going for the optional challenge.

This project emphasizes practical data manipulation using Python, enhancing your ability to navigate and modify complex data structures.

