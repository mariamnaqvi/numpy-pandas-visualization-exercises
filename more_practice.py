import pandas as pd
import numpy as np
from collections import Counter

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]

#using pandas

fruits = pd.Series(['mango', 'kiwi', 'strawberry', 'guava', 'pineapple','mandarin orange'])

fruits.str.upper()

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension 
# syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

fruits.str.title()

# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

fruits_with_more_than_two_vowels = fruits.str.count(r'[aeiou]')

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

result = fruits.map(lambda c: sum([Counter(c.lower()).get(i, 0) 
                                   for i in list('aeiou')]) == 2)

