a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

import numpy as np

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

