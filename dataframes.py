#1 Copy the code from the lesson to create a dataframe full of student grades.
from pydataset import data
import pandas as pd
import numpy as np

np.random.seed(123)
students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                           'math': math_grades,
                           'english': english_grades,
                           'reading': reading_grades})

#a.Create a column named passing_english that indicates whether each student has a passing grade in english.
df['passing english'] = (df['english'] > 70)

#b Sort the english grades by the passing_english column. How are duplicates handled?
df.sort_values(by='english', ascending=False)
    #sorts dupes by index
    
#c Sort the english grades first by passing_english and then by student name. 
# All the students that are failing english should be first, 
# and within the students that are failing english they should be ordered alphabetically. 
# The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
df.sort_values(by=['passing english', 'name'])

#d Sort the english grades first by passing_english, 
# and then by the actual english grade, similar to how we did in the last step.
df.sort_values(by= ['passing english', 'english'], ascending = [False, False])

#e Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.
df['overall_grade'] = ((df.math + df.english + df. reading)/3)

#2 
mpg = data('mpg')

#a how many rows and columns are there?
mpg.shape
    #(234, 11), 234 rows, 11 columns

#b what are the data types of each column?
mpg.info()
'''
 0   manufacturer  234 non-null    object 
 1   model         234 non-null    object 
 2   displ         234 non-null    float64
 3   year          234 non-null    int64  
 4   cyl           234 non-null    int64  
 5   trans         234 non-null    object 
 6   drv           234 non-null    object 
 7   cty           234 non-null    int64  
 8   hwy           234 non-null    int64  
 9   fl            234 non-null    object 
 10  class         234 non-null    object 
 '''
 
 #c summarize the dataframe with .info and .describe
 mpg.describe()
 '''
 count	234.000000	234.000000	234.000000	234.000000	234.000000
mean	3.471795	2003.500000	5.888889	16.858974	23.440171
std	1.291959	4.509646	1.611534	4.255946	5.954643
min	1.600000	1999.000000	4.000000	9.000000	12.000000
25%	2.400000	1999.000000	4.000000	14.000000	18.000000
50%	3.300000	2003.500000	6.000000	17.000000	24.000000
75%	4.600000	2008.000000	8.000000	19.000000	27.000000
max	7.000000	2008.000000	8.000000	35.000000	44.000000
'''
#d-e rename the cty column to city, and the hwy column to highway
mpg = mpg.rename(columns = {'cty':'city', 'hwy':'highway'})

#f Do any cars have better city mileage than highway mileage?
mpg[mpg.city > mpg.highway]
    # no results returned, so no, no cars have better city mileage than highway

#g Create a column named mileage difference that has the difference between city and highway mileage
mpg['mileage_difference'] = (mpg.highway - mpg.city)

#h Which car has the highest mileage difference?
mpg.sort_values(by = 'mileage_difference', ascending = False) 
    #honda civic and volkswagen beetle

#i Which compact class car has the lowest highway mileage, the best?
mpg[mpg['class' == 'subcompact'].sort_values(by = 'highway', ascending = False)
    # best is a 1999 volkswagen beetle

mpg[mpg['class' == 'subcompact'].sort_values(by = 'highway', ascending = True)
    #worst is a 2008 ford mustang

#j create a column named average_mileage that takes the average mileage of the car
mpg['average_mileage'] = (mpg.city + mpg.highway)/2

# which dodge car has the best avg mileage, the worst?
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by = 'average_mileage', ascending = False)
    #best is a 1999 dodge caravan 
mpg[mpg['manufacturer'] == 'dodge'].sort_values(by = 'average_mileage', ascending = True)
    # worst is a 2008 dodge ram 1500 pickup

#3. 
mammals = data('Mammals')
data('Mammals', show_doc = True)

# How many rows and columns?
mammals.shape
    # 107 rows, 4 columns

# What are the data types?
mammals.dytpes
'''
weight      float64
speed       float64
hoppers        bool
specials       bool
dtype: object
'''

# Summarize the dataframe with .info and .describe
mammals.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 107 entries, 1 to 107
Data columns (total 4 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   weight    107 non-null    float64
 1   speed     107 non-null    float64
 2   hoppers   107 non-null    bool   
 3   specials  107 non-null    bool   
dtypes: bool(2), float64(2)
memory usage: 2.7 KB
'''
mammals.describe()
'''
            weight	speed
count	107.000000	107.000000
mean	278.688178	46.208411
std	    839.608269	26.716778
min	    0.016000	1.600000
25%	    1.700000	22.500000
50%	    34.000000	48.000000
75%	    142.500000	65.000000
max	    6000.000000	110.000000
'''
# what is the weight of the fastest animal?
mammals.sort_values(by = 'speed', ascending = False)
    #55 units

# what is the overall percentage of specials?
truemask=mammals['specials'] == True
falsemask = mammals['specials'] == False
mammals[truemask].count() / (mammals[truemask].count() + mammals[falsemask].count())

    #9.3458%

# How many animals are hoppers that are aboe the median speed? waht percentage is this?
median = mammals.speed.median()
hop = (mammals.speed > median) & (mammals.hoppers == True)
fast_hops = mammals[hop]
    # 7 fast hoppers
round((len(fast_hops) / len(mammals)) * 100, 2)
    #6.54