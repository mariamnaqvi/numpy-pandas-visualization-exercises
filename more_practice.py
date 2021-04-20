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

fruits_with_more_than_two_vowels = fruits.str.count('[aeiou]')

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

result = fruits.map(lambda c: sum([Counter(c.lower()).get(i, 0) 
                                   for i in list('aeiou')]) == 2)

fruits[result]

# Exercise 5 - make a list that contains each fruit with more than 5 characters

# Vanilla Python method
def fruits_with_5 (fruits):
    new_list = []
    for fruit in fruits:
        if len(fruit) > 5:
            new_list.append(fruit)
    return new_list

#list comp method   
fruits_morethan5 = [f for f in fruits if len(f) > 5]

#using pandas

fruits_morethan5 = fruits[fruits.apply(lambda x: len(str(x)) > 5)]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters

fruits_with5 = fruits[fruits.apply(lambda fruit: len(str(fruit)) == 5)]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters

fruits_lessthan5 = fruits[fruits.apply(lambda fruit: len(str(fruit)) < 5)]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

char_infruit = fruits.apply(lambda fruit: len(fruit))

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

fruits_with_letter_a = fruits[fruits.str.contains('a')]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

even_numbers = numbers[numbers.apply(lambda n: n % 2 == 0)]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

odd_numbers = numbers[numbers.apply(lambda n: n % 2 == 1)]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

positive_numbers = numbers[numbers.apply(lambda n: n > 0)]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

negative_numbers = numbers[numbers.apply(lambda n: n < 0)]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

two_ormore_numerals = numbers[numbers.apply(lambda n: len(str(abs((n)))) >= 2)]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

numbers_squared = numbers ** 2

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

odd_negative_numbers = numbers[numbers.apply(lambda n: (n < 0) & (n % 2 == 1))]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

numbers_plus_5 = numbers + 5



