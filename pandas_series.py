import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fruits = pd.Series(["kiwi", "mango", "strawberry", "pineapple", 
                    "gala apple", "honeycrisp apple", "tomato", 
                    "watermelon", "honeydew", "kiwi", "kiwi", 
                    "kiwi", "mango", "blueberry", "blackberry", 
                    "gooseberry", "papaya"])
# Exercises Part I
#1 Determine the number of elemets in fruits
print(fruits.size) #17 elements

#2 Output only the index from fruits
ind = fruits.index 
print(ind)

#3 Output only the values from fruits
val = fruits.values
print(val)

#4 confirm the datatype of the values in fruits
data_type = fruits.dtype
print(data_type)

#5 output only the first five values from fruits, last 3 values, and 2 random values
first = fruits.head()
last = fruits.tail(3)
ran = fruits.sample(2)
print(first, last, ran)

#6 Run the .describe() function on fruits to seee what information it returns when called
#  on a series with string values
fruits.describe()
    # gives count 17, unique 13, most common is kiwi with 4

#7 Run the code necessary to produce only the unique string values from fruits
uniq_fruits = fruits.value_counts()

#8 Determine how many times each unique string appears in fruits
print(uniq_fruits)
    # kiwi has 4, mango has 2, and all the rest only appear once

#9 what is the most frequent string value?
print(unique_fruits)
    #kiwi is the most common

#10 What is the least frequent?
print(unique_fruits)
 # all but kiwi and mango only occur once. 

# Exercises Part II

#1 Capitalize all the string values in fruits
fruits.str.title()
    #answer
    '''
    0                 Kiwi
    1                Mango
    2           Strawberry
    3            Pineapple
    4           Gala Apple
    5     Honeycrisp Apple
    6               Tomato
    7           Watermelon
    8             Honeydew
    9                 Kiwi
    10                Kiwi
    11                Kiwi
    12               Mango
    13           Blueberry
    14          Blackberry
    15          Gooseberry
    16              Papaya
    dtype: object
    '''
#2 Count the letter "a" in all the string values
fruits.str.count('a')
    #answer
    '''
    0     0
    1     1
    2     1
    3     1
    4     3
    5     1
    6     1
    7     1
    8     0
    9     0
    10    0
    11    0
    12    1
    13    0
    14    1
    15    0
    16    3
    dtype: int64
    '''

#3 Output the number of vowels in each and every string element
fruits.str.count(r'[aeiou]')
    #answer
    '''
    0     2
    1     2
    2     2
    3     4
    4     4
    5     5
    6     3
    7     4
    8     3
    9     2
    10    2
    11    2
    12    2
    13    3
    14    2
    15    4
    16    3
    dtype: int64
    '''
#4 Write the code to get the longest string value from fruits
fruits[fruits.str.len().idxmax()]
    # honeycrisp apple

#5 Write the code to get the string values with 5 or more letters
    fruits[fruits.str.len() >= 5]
    # fruits longer than 5

#6 Use the .apply method with a lambda function to find the fruits containing 
# the letter "o" two or more times
mask = fruits.apply(lambda x: True if x.count('o') >= 2 else False)
fruits[mask]
    #tomato and Gooseberry 

#7 write the code to get only the string values containing the substring "berry"
fruits[fruits.str.contains('berry')]
    # Strawberry, Blackberry, blueberry, and gooseberry

#8 Write the code to gete only the string values containing the substring "apple".
fruits[fruits.str.contains('apple')]
    # Pineapple, Gala apple, and Honeycrisp apple

#9 Which string value contains the most vowels. 
maxvow = fruits[max(fruits.str.count(r'[aeiou]'))]

#10 Which string has the least vowels
minvow = fruits[min(fruits.str.count(r'[aeiou]'))]

#Exercises Part III.i
letter = pd.Series(list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'))
#1 Which letter occurs most frequently?
maxlet = letter[letter.value_counts().max()]
    # y 
    
#2 Which letter occurs least frequently?
minet = letter.value_counts().idxmax()
    # d 

#3 How many vowels are in the series?
vowels = letter[letter.apply(lambda x: True if x in ('aeiou') else False)]
vowels.value_counts().sum()
    # o : 8, a : 8, u : 7, e: 6, i : 5
    # 34 returned

#4 How many consonants are in the series?
consonants = letter[letter.apply(lambda x: False if x in ('aeiou') else True)]
consonants.value_counts().sum()
# y  :  13, p  :  12, w  :  10, n  :   9, m  :   9, k  :  9, b   :  9,
# c  :   8, r  :   8, x  :   8, h  :   8, d  :   8, q  :  8, v  :   7, 
# z  :   7, f  :   6, j  :   6, s  :   5, g  :   5, l  :  4, t  :   7
#166 returned

#5 Create a series that has all the same letters but uppercased
capletter = letter.str.upper()

#6 Create a bar plot of frequencies of the most commonly occuring letters
fig = capletter.value_counts().head(6).plot.bar(color='green', width=.9)
plt.title('Letter frequencies')
plt.xticks(rotation=0)
plt.xlabel('Letter')
plt.ylabel('Frequency')

#Part III.ii
numbers = pd.Series(['$796,459.41', '$278.60', '$482,571.67', 
                     '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', 
                     '$87,231.01', '$1,509,175.45', '$4,138,548.00', 
                     '$2,848,913.80', '$594,715.39', '$4,789,988.17', 
                     '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', 
                     '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', 
                     '$769,681.94', '$452,650.23'])

#1  What is the data type of the numbers series?
    numbers.dtype
    # they are objects

#2 How many elements are in the number series?
    numbers.size

#3 Perform the necessary manipulations by accessing by accessing series attributes and 
# and methods to convert the numbers series to a numeric data type
numbers = numbers.str.replace('$','').str.replace(',','').astype(float)

#4 Discover the maximum value from the series
maxnum = numbers.max()

#5 Discover the minimum value from the series
minnum = numbers.min()

#6 Discover the range of the series
range_of_num = maxnum - minnum 

#7 Bin the data into 4 equally sized intervals or bins
binned = pd.cut(numbers, 4).value_counts()

#8
n_bins = [0, 1197427, (1197427 * 2), (1197427 *3), (1197427*4)]
plt.hist(binned, bins = n_bins)

# Part III.iii
exam_scores = pd.Series([60, 86, 75, 62, 93, 71, 60, 
                         83, 95, 78, 65, 72, 69, 81, 
                         96, 80, 85, 92, 82, 78])
#1. How many elements are in the exam scores series?
exam_scores.size   
    # 20 values

#2 Run the code to discover the min/max, mean, and median for the series
exam_scores.describe()
    # mean: 78.15, min 60, max 96, and median score 79

#3 
exam_scores.plot.hist(color='firebrick', width=.9)
plt.title('Grades')
plt.xticks(rotation=0)
plt.xlabel('Student Tests')
plt.ylabel('Score')

#4 
curved_scores = exam_scores + 4

#5 
grade_bins = [0 , 70 , 75, 80 , 90 , 100]
bin_labels = ['F', 'D', 'C', 'B', 'A']
letter_scores = pd.cut(curved_scores, bins = grade_bins, labels = bin_labels)

#6
letter_scores.value_counts().sort_index().plot.barh(color=['red','orange','yellow','green','blue'], 
                                                    ec = 'black', width =.9)
plt.title('Letter Grades')
plt.xticks(rotation=0)
plt.xlabel('Number of Scroes')
plt.ylabel('Letter Grade')