#  Use pandas to create a Series named fruits from the following list:
    ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.

fruits.size
# returns 17 elements

# 2. Output only the index from fruits.

fruits.index.tolist()

# 3. Output only the values from fruits.

fruits.values

# 4. Confirm the data type of the values in fruits.

fruits.dtype

# 5. a) Output only the first five values from fruits.  

fruits.head(5)

#  b) Output the last three values.

fruits.tail(3)

# c) Output two random values from fruits.

fruits.sample(2)

# 6. Run the .describe() on fruits to see what information it returns when called on a Series with string values.

fruits.describe()
# returns 
# count       17
# unique      13
# top       kiwi
# freq         4
# dtype: object

# 7. Run the code necessary to produce only the unique string values from fruits.

# 8. Determine how many times each unique string value occurs in fruits.

# 9. Determine the string value that occurs most frequently in fruits.

# 10. Determine the string value that occurs least frequently in fruits.

