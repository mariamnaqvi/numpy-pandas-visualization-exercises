# solve each using vanilla python.

# solve each using list comprehensions.

# solve each by using a pandas Series for the data structure instead of lists 
# and using vectorized operations instead of loops and list comprehensions.


import pandas as pd
import numpy as np
from collections import Counter

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 1 - rewrite the above example code using list comprehension syntax. 
# Make a variable named uppercased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI', etc...]

# using vanilla python
uppercased_fruits = []
for fruit in fruits:
    uppercased_fruits.append(fruit.upper())
print (f'uppercased_fruits: {uppercased_fruits}')

# using list comprehension
uppercased_fruits = [fruit.upper() for fruit in fruits]

#using pandas
fruits = pd.Series(['mango', 'kiwi', 'strawberry', 'guava', 'pineapple','mandarin orange'])

fruits.str.upper()

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension 
# syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# using vanilla python
capitalized_fruits = []

for fruit in fruits:
    capitalized_fruits.append(fruit.title())

# using list comprehension
capitalized_fruits = [fruit.title() for fruit in fruits]

#using pandas
fruits.str.title()

# Exercise 3 - Use a list comprehension to make a variable named 
# fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
# using vanilla python

# using list comprehension

#using pandas
fruits_with_more_than_two_vowels = fruits.str.count('[aeiou]')

# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
# using vanilla python
fruits_with_more_than_two_vowels = []

def count_vowels(fruit):
    count = 0
    for letter in fruit:
        if letter.lower() in 'aeiou':
            count += 1
    return count

for fruit in fruits:
    if count_vowels(fruit) > 2:
        fruits_with_more_than_two_vowels.append(fruit)

# using list comprehension
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]

#using pandas
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
fruits_morethan5 = [fruit for fruit in fruits if len(fruit) > 5]

#using pandas

fruits_morethan5 = fruits[fruits.apply(lambda x: len(str(x)) > 5)]

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
# using vanilla python
exactly5_fruit = []
for fruit in fruits:
    if len(fruit) == 5:
        exactly5_fruit.append(fruit)


# using list comprehension
exactly5_fruit = [fruit for fruit in fruits if len(fruit) == 5]


#using pandas
fruits_with5 = fruits[fruits.apply(lambda fruit: len(str(fruit)) == 5)]

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
# using vanilla python
lessthan5_fruit = []
for fruit in fruits:
    if len(fruit) < 5:
       lessthan5_fruit.append(fruit) 

# using list comprehension
lessthan5_fruit = [fruit for fruit in fruits if len(fruit) < 5]

#using pandas
fruits_lessthan5 = fruits[fruits.apply(lambda fruit: len(str(fruit)) < 5)]

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
# using vanilla python
char_fruit = []
for fruit in fruits:
    char_fruit.append(len(fruit))

# using list comprehension
char_fruit = [len(fruit) for fruit in fruits]

#using pandas
char_infruit = fruits.apply(lambda fruit: len(fruit))

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
# using vanilla python
fruits_with_letter_a = []
for fruit in fruits:
    if fruit.find('a') >= 1:
        fruits_with_letter_a.append(fruit)

# using list comprehension
fruits_with_letter_a = [fruit for fruit in fruits if fruit.find('a') >= 1]

#using pandas
fruits_with_letter_a = fruits[fruits.str.contains('a')]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
# using vanilla python
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

# using list comprehension
even_numbers = [number for number in numbers if number % 2 == 0]

#using pandas
even_numbers = numbers[numbers.apply(lambda n: n % 2 == 0)]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
# using vanilla python
odd_numbers = []
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)

# using list comprehension
odd_numbers = [number for number in numbers if number % 2 == 1]

#using pandas
odd_numbers = numbers[numbers.apply(lambda n: n % 2 == 1)]

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
# using vanilla python
positive_numbers = []
for number in numbers:
    if number > 0:
        positive_numbers.append(number)

# using list comprehension
positive_numbers = [number for number in numbers if number > 0]

#using pandas
positive_numbers = numbers[numbers.apply(lambda n: n > 0)]

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
# using vanilla python
negative_numbers = []
for number in numbers:
    if number < 0:
        negative_numbers.append(number)

# using list comprehension
negative_numbers = [number for number in numbers if number < 0]

#using pandas
negative_numbers = numbers[numbers.apply(lambda n: n < 0)]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
# using vanilla python
two_or_more = []
for number in numbers:
    if len(str(abs(number)))>=2:
        two_or_more.append(number)

# using list comprehension
two_or_more = [number for number in numbers if len(str(abs(number))) >= 2]

#using pandas
two_ormore_numerals = numbers[numbers.apply(lambda n: len(str(abs((n)))) >= 2)]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
# using vanilla python
numbers_squared = []
for number in numbers:
    numbers_squared.append(number * number)

# using list comprehension
numbers_squared = [number * number for number in numbers]

#using pandas
numbers_squared = numbers ** 2

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
# using vanilla python
odd_negative_numbers = []
for number in numbers:
    if number < 0 and (number % 2 == 1):
        odd_negative_numbers.append(number)

# using list comprehension
odd_negative_numbers = [number for number in numbers if number < 0 and (number % 2 == 1)]

#using pandas
odd_negative_numbers = numbers[numbers.apply(lambda n: (n < 0) & (n % 2 == 1))]

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 
# using vanilla python
numbers_plus_5 = []
for number in numbers:
    numbers_plus_5.append(number + 5)

# using list comprehension
numbers_plus_5 = [number + 5 for number in numbers]

#using pandas
numbers_plus_5 = numbers + 5



