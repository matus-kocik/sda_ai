# Sold out (Python)

After learning manual calculation techniques, you're now ready to automate similar tasks using loops and conditionals, significantly reducing the amount of code you need to write.

## Tasks

### [√] Average sales

Calculate the average sales income of the albums using a for loop.

1. [√] The **data.py** file contains a variable named **average_sale** the value of which is the average sale of the eight albums.

2. [√] A for loop performs the addition part of the calculation.


### [√] Average age

Calculate the average age of the albums.

1. [√] The **data.py** file contains a variable named **average_age** the value of which is the average age of the eight albums.

2. [√] A for loop performs a part of the calculation.

### [√] Newest and oldest albums

Identify the newest and oldest albums using **for** and **if**.

1. [√] The **data.py** file contains a variable named **newest_album** the value of which is the most recently released album (object) from the **best_selling_albums** list.

2. [√] A for loop and conditional statement inside perform a part of the calculation.

3. [√] The **data.py** file contains a variable named **oldest_album** the value of which is the oldest album (object) released from the **best_selling_albums** list.

4. [√] A for loop and conditional statement inside perform a part of the calculation.

### [√] The albums of Eagles

Summarize the sales of the Eagles albums.

1. [√] The **data.py** file contains a variable named **albums_of_eagles** which is an object.

2. [√] One key in the object is named **sales** with a value being the sum of the sales of the two Eagles albums (using dot and bracket notations).

3. [√] Another key in the object is named **is_both_soft_rock** with a boolean value. Two for loops check if both Eagles albums' genre lists contain the soft rock genre. If both do, **is_both_soft_rock** is **true**; otherwise, it's **false**.

### [√] Do you like it?

Add a new key to each album. Use logical operators and **if/else** chains to assign values based on the artist and title. The value of the new key, **i_like_it**, depends on your preference, ensuring at least one album has a **true** value.

1. [√] Every album in the **best_selling_albums** list includes an **i_like_it** key with a boolean value, reflecting personal preference. At least one album must have **true** as its value.

2. [√] The new key is assigned using a single assignment operator within a conditional statement nested in a for loop, utilizing both bracket and dot notation.

## Hints

- Combine conditions within **if/else** statements using logical operators (**and, or**) and create multiple conditions to set the **i_like_it** key's value based on both artist and title. Here's an example in Python syntax:

```python
if something['first_key'] == "A" and something['second_key'] == "B":
    ...
elif something['first_key'] == "C" and something['second_key'] == "D":
    ...
elif something['first_key'] == "F" or something['second_key'] == "E":
    ...
```

- Focus on mastering **for** and **while** loops as they are fundamental in Python for iterating through data. Other iteration methods like list comprehensions or the **map** and **filter** functions will be covered later.

- Revisit previous projects to review your solutions and the provided guides and hints for further clarification.

