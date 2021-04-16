import numpy as np
# create working np.array
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1 How many negative numbers are there?
def negnum(array):
    neg = array[array < 0]
    count = 0
    for x in neg:
        count += 1
    return count
    # 4 neg numbers

#2 How many positive numbers are there?
def posnum(array):
    pos = array[array > 0]
    count = 0
    for x in pos:
        count += 1
    return count
    # 8 pos numbers

#3 How many positive even numbers
def posnum(array):
    pos = array[array > 0]
    poseven = pos[pos % 2 == 0]
    count = 0
    for x in poseven:
        count += 1
    return count
    # 3 numbers

#4 If you were to add 3 to each data point, how many positive numbers would there be?
def addnum(array):
    add = array + 3 
    pos = add[add > 0]
    count = 0
    for x in pos:
        count += 1
    return count
    # 10 positive numbers
#5 if you squared each number, what would the mean and stdev be?
def sqnum(array):
    sq = a ** 2 
    std = np.std(sq)
    mn = np.mean(sq)
    return std, mn 
    # std : 144.0243035046516, mean : 74
#6 center the data set by subtracting the mean from every set
def cent(array):
    mn = np.mean(array)
    center = array - mn 
    return center
    # centered array : array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0., -10.])

#7
def zscore(array):
    mean = np.mean(array)
    std = np.std(array)
    numerator = array - mean
    zscore = (numerator / std)
    return zscore
    # zscores: array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
    #                 -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
    #                  0.        , -1.24034735])

#8 More Numpy exercises....


# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)
# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)
# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)
# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum(a) / len(a)
# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
for x in a:
    product_of_a = 1
    product_of_a = product_of_a * x
# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [x ** 2 for x in a]
# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [x for x in a if x % 2 != 0]
# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [x for x in a if x % 2 == 0]
## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

b = np.array(b)
sum_of_b = np.sum(b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = np.amin(b)
# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = np.amax(b)

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = np.mean(b)
# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
#product_of_b = 1
#for row in b:
 #   for number in row:
  #      product_of_b *= number
    
product_of_b = np.prod(b)

# Exercise 6 - refactor the following to use numpy to find the list of squares 
#squares_of_b = []
#for row in b:
  #  for number in row:
   #     squares_of_b.append(number**2)

squares_of_b = b 
# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 != 0]
# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b = b[b % 2 == 0]
# Exercise 9 - print out the shape of the array b.
shape = np.shape(b)
print(shape)
# Exercise 10 - transpose the array b.
transposed_b = np.transpose(b)
# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
newarr= b.reshape(1,6)
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
newarr2 = b.reshape(6,1)
## Setup 3
cl = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
c = np.array(cl)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
minc= np.min(c)
maxc= np.max(c)
sumc= np.sum(c)
prodc= np.prod(c)
# Exercise 2 - Determine the standard deviation of c.
stdev = np.std(c)
# Exercise 3 - Determine the variance of c.
variance = np.var(c)
# Exercise 4 - Print out the shape of the array c
shapec = np.shape(c)
# Exercise 5 - Transpose c and print out transposed result.
transposed_c = np.transpose(c)
print(transposed_c)
# Exercise 6 - Get the dot product of the array c with c. 
dotprod = np.dot(c, cl)
# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
sumall = np.sum(c * transposed_c)
# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
prodall = np.prod(c * transposed_c)
## Setup 4
dl = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d = np.array(dl)
print(d)
# Exercise 1 - Find the sine of all the numbers in d
sind = np.sin(d)
# Exercise 2 - Find the cosine of all the numbers in d
cosind= np.cos(d)
# Exercise 3 - Find the tangent of all the numbers in d
tand = np.tan(d)
# Exercise 4 - Find all the negative numbers in d
neg = d[d < 0]
# Exercise 5 - Find all the positive numbers in d
pos = d[d > 0]
# Exercise 6 - Return an array of only the unique numbers in d.
uniquearrd = np.unique(d)
# Exercise 7 - Determine how many unique numbers there are in d.
uniquenum = np.shape(uniquearrd) # 11 unique numbers
# Exercise 8 - Print out the shape of d.
shaped = np.shape(d)
print(shaped)
# Exercise 9 - Transpose and then print out the shape of d.
print(np.shape(np.transpose(d)))
# Exercise 10 - Reshape d into an array of 9 x 2
reshaped = d.reshape(9,2)