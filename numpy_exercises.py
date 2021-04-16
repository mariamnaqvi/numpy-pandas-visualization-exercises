import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there? 

count_negatives = len(a [a < 0 ])  
print (count_negatives)

# 2. How many positive numbers are there?

count_positives = len(a [a > 0 ])
print (count_positives)

# 3. How many even positive numbers are there?

count_even_pos = len([n for n in a if n > 0 and n % 2 ==0])
print (count_even_pos)

# 4. If you were to add 3 to each data point, how many positive numbers would there be?

count_pos_add3 = len([n for n in a if n + 3 > 0])
print (count_pos_add3) 

# 5. If you squared each number, what would the new mean and standard deviation be?

squared_list = [n ** 2 for n in a]
mean_of_squared = np.mean(squared_list) 
print (mean_of_squared) 

std_of_squared = round(np.std(squared_list), 3)
print (std_of_squared)


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

centered_data =  a - a.mean()
print (centered_data)

# 7. Calculate the z-score for each data point. 

z_score =  centered_data/std
print (z_score)

# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions. 

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

sum_of_a = np.sum(a)
print (sum_of_a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = np.min(a)
print (min_of_a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = np.max(a)
print (max_of_a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = np.mean(a)
print (mean_of_a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = np.product(a)
print (product_of_a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

