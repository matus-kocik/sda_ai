# The Pizza Madness (Python)

You started working as a developer for a pizza company. Unfortunately, their sales program is not up to scratch, and it is your job to fix some errors and expand the program with new functions.

## Tasks

### [ ] String repeat

The pizza company's customers have unique tastes; they prefer pizza names to be stylized in a particular way. Create a Python function named **string_repeat()** that takes two arguments, **number** (an integer) and **str** (a string), and returns the **str** repeated **number** times.

1. [ ] The **string_repeat(2, "HawaiiPizza")** function should return the string **HawaiiPizzaHawaiiPizza**.

### [ ] No whitespaces

Due to a design oversight, the pizza names are too long for the website's layout. The quickest fix is to remove all spaces from the names. Write a Python function named **no_space()** that takes a string **str** and returns it without any spaces.

1. [ ] The **no_space()** function must return a string with all whitespaces removed.

### [ ] Number to string

The order system is flawed; it can only process string inputs. Write a Python function named **number_to_string()** that accepts an **integer** and returns it as a **string**.

1. [ ] The **number_to_string()** function should return a **string**.

### [ ] Boolean to string

There are still issues with the ordering system. Create a Python function named **boolean_to_string()** that takes a **boolean** and returns it as a **string**.

1. [ ] The **boolean_to_string()** function should return a **string**.

### [ ] Abbreviate a Pizza name

To simplify the waitstaff's job, we need a function to abbreviate pizza names. Write a Python function named **abbrev_name()** that accepts a **string** consisting of two words and returns the initials of each word, separated by a dot.

1. [ ] The **abbrev_name("Hawaii Pizza")** function should return **"H.P"**.

### [ ] Pizza length

Create a Python function named **name_length()** that takes a **string** and returns a list where each element's length is appended next to it.

1. [ ] The **name_length("hawaii pizza")** function should return **["hawaii 6", "pizza 5"]**.

### [ ] Remove the first and last element

Due to an error, two extra orders were added by mistake. Write a Python function named **remove_orders()** that takes a **string** of numbers separated by commas, converts it into a list, removes the first and last elements, and then returns the modified list as a string.

1. [ ] The **remove_orders("1,2,3,4")** function should return **"2,3"**.

### [ ] The menu

Implement a Python function named **food_menu()** that takes a list of food items as an argument and returns a new list with each item prefixed by its position in the original list.

1. [ ] The **food_menu(["Hawaii Pizza", "Diablo Pizza"])** function should return **["1. Hawaii Pizza", "2. Diablo Pizza"]**.

## General requirements

- Maximize the use of Python's built-in functions for efficiency.