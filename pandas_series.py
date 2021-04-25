import numpy as numpy
import pandas as pd
import matplotlib.pyplot as plt

#  Use pandas to create a Series named fruits from the following list:
["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])
type(fruits)

# Use Series attributes and methods to explore your fruits Series.

# 1. Determine the number of elements in fruits.

fruits.size
# returns 17 elements
# or 
fruits.shape

# 2. Output only the index from fruits.

fruits.index.tolist()

# or
list(fruits.index)

# 3. Output only the values from fruits.

fruits.values

# 4. Confirm the data type of the values in fruits.

fruits.dtype

# 5. a) Output only the first five values from fruits.  

fruits.head() # default is 5

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

fruits.unique()

fruits.nunique() #gives number of uniques

# 8. Determine how many times each unique string value occurs in fruits.

fruits.value_counts() # returns a new series

# 9. Determine the string value that occurs most frequently in fruits.

fruits.mode()

# or

fruits.value_counts()[:1].sort_values(ascending=False)

# or 

fruits.value_counts().head(1)

# or

fruits.value_counts().idxmax() # returns index with max value

# or 

fruits.value_counts().nlargest(n=1, keep = 'all') # in case of a tie, return all, by default n = 5

# 10. Determine the string value that occurs least frequently in fruits.

fruits.value_counts()[:-1].sort_values(ascending=True)

# or

fruits.value_counts().nsmallest(n=1, keep = 'all')

# ---------------------------------------------------------

# Exercises Part II

# 1. Capitalize all the string values in fruits.

fruits.str.title()

# 2. Count the letter "a" in all the string values (use string vectorization).

fruits.str.count('a').sum()

# 3. Output the number of vowels in each and every string value.

def count_vowels(fruit):
    return len([letter for letter in fruit if letter.lower() in 'aeiou'])

vowels_count = fruits[fruits.apply(count_vowels)]

# or alt solution 

fruits.str.count('a|e|i|o|u')

# to get a table like below that gives the fruit name with its corresponding vowel count

new_df = fruits.reset_index() # add another index col

new_df['vowel_count'] = fruits.str.count('a|e|i|o|u') # add a new vowel count col and count vowels in each fruit

new_df2 = new_df.drop(columns = ['index']) # drop the index col

new_df3 = new_df2.rename(columns = {0: 'fruit name'}) # rename the 0 col to fruit name

'''
returns 

    fruit name	    vowel_count
0	kiwi	            2
1	mango	            2
2	strawberry	        2
3	pineapple	        4
4	gala apple	        4
5	honeycrisp apple	5
6	tomato	            3
7	watermelon  	    4
8	honeydew	        3
9	kiwi	            2
10	kiwi	            2
11	kiwi	            2
12	mango	            2
13	blueberry	        3
14	blackberry	        2
15	gooseberry	        4
16	papaya	            3
'''

# to to group strings by the number of occurrences of each vowel

fruits.str.count('[aeiou]').value_counts()

# 4. Write the code to get the longest string value from fruits.

# to get the length of all fruits in the series

lengths = fruits.apply(lambda f: len(f))

# gives index of longest string
lengths.idxmax()

# to get the name of the fruit with the longest length
fruits[lengths.idxmax()]

# alt solution
longest = fruits.apply(len).nlargest(1)
fruits[longest.idxmax()]

# or

max(fruits, key=len)

# 5. Write the code to get the string values with 5 or more letters in the name.

fruits[fruits.str.len() >= 5]

# 6. Use the .apply method with a lambda function to find the fruit(s) containing the letter "o" two or more times.

fruits[fruits.apply(lambda fruit: fruit.count('o') >= 2)]

# 7. Write the code to get only the string values containing the substring "berry".

fruits[fruits.str.contains('berry')]

# 8. Write the code to get only the string values containing the substring "apple".

fruits[fruits.str.contains('apple')]

# 9. Which string value contains the most vowels?

fruits[fruits.str.lower().str.count(r'[aeiou]').max()]

# alt 1
fruits[fruits.str.count('[aeiou]').max()]

# alt 2
fruits[fruits.str.count('[aeiou]').idxmax()]

# ---------------------------------------------------------

# Exercises Part III 

# Letters Series

# 1. Which letter occurs the most frequently in the letters Series?
letters = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy
'))
letters.value_counts().idxmax()

# or 

letters.mode() # returns y 

# 2. Which letter occurs the Least frequently?

#value_counts gives count of each letter
letters.value_counts().idxmin() # returns l

#  3. How many vowels are in the Series?

letters.str.count('[aeiou]').sum() # .count tells you which index is a vowel, .sum adds up the vowels
# returns 34 vowels

# alt 1
letters.str.count('[aeiou]') # returns boolean values where 1 is True for vowel
letters.str.count('[aeiou]').value_counts() # returns the count of 0 and 1 where 1 is true

# 4. How many consonants are in the Series?

letters.str.count('[bcdfghjklmnpqrstvwxyz]').sum()
# returns 166 consonants

# or use ~ to check letters not in vowels
(~letters.str.lower().isin(['a', 'e', 'i', 'o', 'u'])).sum()

# 5. Create a Series that has all of the same letters but uppercased.

upper_series = letters.str.upper()

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.

letters.value_counts().head(6) # gives the 6 most commonly occuring letters

fig = upper_series.value_counts().head(6).plot.bar(color = 'blue', width =0.8)
plt.title('Letter frequencies')
plt.xticks(rotation = 0)
plt.xlabel('letters')
plt.ylabel('frequency')
plt.show()

# ---------------------------------------------------------

# Numbers Series

# 1. What is the data type of the numbers Series?

numbers.dtype

# 2. How many elements are in the number Series?

numbers.size 

# 3. Perform the necessary manipulations by accessing Series attributes and methods to convert the numbers Series to a numeric data type.

numbers = numbers.str.replace('$','').str.replace(',','') # remove dollar signs and commas

numbers = numbers.astype('float') # convert dtype to numeric

# 4. Run the code to discover the maximum value from the Series.

max_number = numbers.max()

# 5. Run the code to discover the minimum value from the Series.

min_number = numbers.min()

# 6. What is the range of the values in the Series?

range_of_vals = max_number - min_number

# 7. Bin the data into 4 equally sized intervals or bins and output how many values fall into each bin.

pd.cut(numbers, 4).value_counts()

# returns
# (-4511.11, 1197705.993]       7
# (3592560.778, 4789988.17]     6
# (1197705.993, 2395133.385]    4
# (2395133.385, 3592560.778]    3

# 8. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

numbers.value_counts(bins=4)
bin_range = [0, 1197427, (1197427 * 2), (1197427 *3), (1197427*4)]
plt.xlabel('Bins')
plt.title('Binned Data')
numbers.plot.hist(numbers, bins = bin_range)

# ---------------------------------------------------------

exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 
                         92, 82, 78])

# 1. How many elements are in the exam_scores Series?

exam_scores.size # returns 20 elements

# 2. Run the code to discover the minimum, the maximum, the mean, and the median scores for the exam_scores Series.

exam_scores.describe()

# 3. Plot the Series in a meaningful way and make sure your chart has a title and axis labels.

exam_scores.plot.hist(color = 'blue', ec = 'black', alpha = .5)

plt.title('Exam Scores Distribution')
plt.xlabel('Scores')
plt.show()

# alt method
# sort the exam scores according to their frequencies
exam_scores.value_counts()

# sorts the index which is the exam score
exam_scores.value_counts().sort_index()

# plot into a histogram >> the grades will be in ascending order due to sorting above
exam_scores.value_counts().sort_index().plot(kind = 'bar', color = 'lime', ec = 'black', alpha = 0.4, rot = 0)

plt.title('Exam Scores Distribution')
plt.xlabel('Score')
plt.ylabel('Number of Students')
plt.show()

# 4. Write the code necessary to implement a curve for your exam_grades Series and save this as curved_grades. 
# Add the necessary points to the highest grade to make it 100, and add the same number of points to every other score in the Series as well.
curved_grades = (100 - exam_scores.max()) + exam_scores

# 5. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. 
# For example, 86 should be a 'B' and 95 should be an 'A'. Save this as a Series named letter_grades.

letter_grades = pd.cut(curved_grades, 4,labels=["D", "C", "B", "A"])

# 6. Plot your new categorical letter_grades Series in a meaninful way and include a title and axis labels.

fig = letter_grades.value_counts().plot.bar(color = 'violet', width =0.8, 
                                            alpha = 0.6)
plt.title('Student Grades')
plt.xticks(rotation = 0)
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.show()