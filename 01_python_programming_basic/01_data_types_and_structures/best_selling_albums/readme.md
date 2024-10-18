# Best selling albums (Python)

In this project, you will work with an existing data structure: the eight best-selling albums of all time. Unlike before, this data is represented as a list with dictionaries in Python. The tasks have been slightly modified to suit this context.

## Tasks

### [√] Calculate average sales income

Calculate the average sales income of the albums. Assign this calculation to a new variable named average_sale.

1. [√] The data.py file contains a variable named average_sale whose value is the calculation of the average sale of the eight albums.

### [√] Calculate average age

Calculate the average age of the albums. First, store the current year in a variable named current_year, then calculate the average age and assign it to another variable called average_age.

1. [√] The data.py file contains a variable named average_age whose value is the calculation of the average age of the eight albums.

### [√] Newest and oldest album

Create a variable named newest_album and assign the most recently released album (dictionary) as its value. Create another variable named oldest_album and assign the oldest album to it.

1. [√] The data.py file contains a variable named newest_album whose value is the most recently released album dictionary from the best_selling_albums list.
2. [√] The data.py file contains a variable named oldest_album whose value is the oldest released album dictionary from the best_selling_albums list.

### [√] Albums of Eagles

The band Eagles has two albums on the list. Create a new variable albums_eagles as a dictionary. Then add a sales key with the sum of the sales of the two albums. Add another key named is_both_soft_rock, and set its value to true by comparing the "soft rock" genres of both albums.

1. [√] The data.py file contains a variable named albums_eagles whose value is a dictionary.
2. [√] One key of the dictionary is sales, with its value being the sum of the sales of the two Eagles albums.
3. [√] Another key of the dictionary is is_both_soft_rock whose value is true if both Eagles albums are classified under "soft rock" genre.

### [√] Add an extra album

Find another album of your choice, collect similar data as the albums in the best_selling_albums list. Make a dictionary out of it and set it as the value of the ninth item in the best_selling_albums list.

1. [√] The best_selling_albums list has a ninth item which is a dictionary containing the same keys as the others. The ninth item is added using the assignment operator and list indexing.

### [√] Like it or not

Add a new i_like_it key to each album dictionary with a boolean value: true if you like the album and false if you do not.

1. [√] Each album dictionary in the best_selling_albums list contains an i_like_it key with a boolean value. The new key is added using the assignment operator, list indexing, and dictionary key assignment.

### Hints

- The data structure you'll be working with (best_selling_albums) should be in the data.py file.
- The single equals sign (=) in Python is used for assignment, not comparison. For comparing equality, Python uses double equals sign (==).
- In Python, comparisons result in boolean values (True or False). You can directly assign this result to a variable.
- Remember to use Python's list and dictionary syntax for accessing and modifying data.
- As with previous projects, ensure accuracy in your implementation. If you encounter difficulties, don't hesitate to seek help or refer back to the materials from previous projects for guidance.

