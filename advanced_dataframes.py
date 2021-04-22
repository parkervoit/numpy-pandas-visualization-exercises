# EXERCISE I
#1 Create a function named get_db_url. It should accept a username, hostname, password, 
# and database name and return a url connection string formatted like in the example at the start of this lesson.
from env import host, user, password
import pandas as pd
import numpy as np
from pydataset import data

from env import host, username, password
def get_emp_url(username, password, host):
    db_url = f'mysql+pymysql://{username}:{password}@{host}/employees'
    return db_url


#2 Use your function to obtain a connection to the employees database
url = get_emp_url(username, password, host)

# 3 Once you have successfuly ran a query
#a make a typo in the database url
employees = pd.read_sql('SELECT * FROM employees LIMIT 5 OFFSET 50', get_db_url()) 
    # I get a NameError when I use the wrong database variable name

db_url = f'mysql+pymysql://{username}:{password}@{host}/emploees'
    # I get an operational error when I misspell the employees database name in the url.

#b Intentionally make an error in your SQL query.
employees = pd.read_sql('SELECT * FROM emploees LIMIT 5 OFFSET 50', get_db_url())
    # I get a programming error, it also returns the error from sql saing table doesnt exist

#4. Read the employees and titles tables into two seperate data frames
employees = pd.read_sql('SELECT * FROM employees', get_db_url())
    #returns a dataframe from the employees table

titles = pd.read_sql('SELECT * FROM titles', get_db_url())
    #returns a dataframe from the titles table

#5 How many rows and columns do you have in each dataframe?
titles.shape
    # 443308 rows × 4 columns
employees.shape
    # 300024 rows × 6 columns 
    # The rows can vary because indivudal employees could have multiple titles

#6 Display the summary statistics for each dataframe
titles.describe(exclude = np.number)
'''
        title	from_date	to_date
count	443308	443308	    443308
unique	7	    6393	    5888
top	    Engin.  1998-10-25	9999-01-01
freq	115003	132	        240124
'''

employees.describe(exclude = np.number)
'''
       birth_date	first_name	last_name	gender	hire_date
count  300024	    300024	    300024	    300024	300024
unique	4750	    1275	    1637	    2	    5434
top	    1952-03-08	Shahab	    Baba	    M	    1985-06-20
freq	95	        295	        226	        179973	132
'''

#7 How many unique titles?
distinct_titles= pd.read_sql('SELECT DISTINCT title FROM titles', get_db_url())
    # 7 unique titles in the title df

titles.title.unique().shape
    # gives me 7 

#8 oldest to-date in the column?
oldest_date = pd.read_sql('SELECT MIN(to_date) FROM titles', get_db_url())
 # 1985-03-01
 
min(titles['to_date'])
    # gives me 1985,3,01
titles.to_date.min()

#9 most recent date?
recent_date = pd.read_sql('SELECT MAX(to_date) FROM titles', get_db_url())
# cur date, 9999-1-1

min(titles['to_date'])
# gives 9999,1,1
 
titles.to_date.max()
# this one also works

#EXERCISE 2

#1 Creating users and roles dfs
users = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['bob', 'joe', 'sally', 'adam', 'jane', 'mike'],
    'role_id': [1, 2, 3, 3, np.nan, np.nan]
})
users

roles = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['admin', 'author', 'reviewer', 'commenter']
})
roles

#2 What are the results of a right join?

# users is left, roles is right, link foreign keys with role_id and id, set indicator to true so I
# can see what is being joined. 

users.merge(roles, how='right', on=None, left_on='role_id', right_on='id', indicator=True)
'''
id_x	name_x	role_id	id_y	name_y	_merge
0	1.0	bob	1.0	1	admin	both
1	2.0	joe	2.0	2	author	both
2	3.0	sally	3.0	3	reviewer	both
3	4.0	adam	3.0	3	reviewer	both
4	NaN	NaN	NaN	4	commenter	right_only
'''
#3 What is the result of using an outer join?

# same as before, but just change how to 'outer', keep foreign key links the same

users.merge(roles,  how='outer', left_on='role_id', right_on='id', indicator=True)
'''
id_x	name_x	role_id	id_y	name_y	_merge
0	1.0	bob	1.0	1.0	admin	both
1	2.0	joe	2.0	2.0	author	both
2	3.0	sally	3.0	3.0	reviewer	both
3	4.0	adam	3.0	3.0	reviewer	both
4	5.0	jane	NaN	NaN	NaN	left_only
5	6.0	mike	NaN	NaN	NaN	left_only
6	NaN	NaN	NaN	4.0	commenter	right_only
'''

# 4 what happens if you try to drop the foreing keys from the DFs and try to merge them?
drop_users = users.drop(columns = 'role_id')
drop_roles = roles.drop(columns = 'id')

# inner join
drop_users.merge(drop_roles, how='inner', indicator=True)
'''
id	name   _merge
'''

# outer join
drop_users.merge(drop_roles, how='outer', indicator=True)
'''
	id	name	_merge
0	1.0	bob	left_only
1	2.0	joe	left_only
2	3.0	sally	left_only
3	4.0	adam	left_only
4	5.0	jane	left_only
5	6.0	mike	left_only
6	NaN	admin	right_only
7	NaN	author	right_only
8	NaN	reviewer	right_only
9	NaN	commenter	right_only
'''

#right join
users.merge(drop_roles, how='right', indicator=True)
'''
	id	name	_merge
0	NaN	admin	right_only
1	NaN	author	right_only
2	NaN	reviewer	right_only
3	NaN	commenter	right_only
'''

#left join
users.merge(drop_roles, how='left', indicator=True)
'''
id	name	_merge
0	1	bob	left_only
1	2	joe	left_only
2	3	sally	left_only
3	4	adam	left_only
4	5	jane	left_only
5	6	mike	left_only
'''
    # Trying to join when foriegn keys are deleted removes the ability for 
    # pandas to merge the dataframes. Instead, it defaults to just stacking the
    # elements and placing NaN values for any missing values.

#5 Load mpg dataset from pydataset
mpg = data('mpg')

#6 output and read the documenation for the mpg dataset
data('mpg', show_doc = True) # check the documentation

'''
PyDataset Documentation (adopted from R Documentation. The displayed examples are in R)

## Fuel economy data from 1999 and 2008 for 38 popular models of car

### Description

This dataset contains a subset of the fuel economy data that the EPA makes
available on http://fueleconomy.gov. It contains only models which had a new
release every year between 1999 and 2008 - this was used as a proxy for the
popularity of the car.

### Usage

    data(mpg)

### Format

A data frame with 234 rows and 11 variables

### Details

  * manufacturer. 

  * model. 

  * displ. engine displacement, in litres 

  * year. 

  * cyl. number of cylinders 

  * trans. type of transmission 

  * drv. f = front-wheel drive, r = rear wheel drive, 4 = 4wd 

  * cty. city miles per gallon 

  * hwy. highway miles per gallon 

  * fl. 

  * class. 

'''

#7 How many rows and columns are in the dataset?
mpg.shape
    # 235 rows x 11 columns

#8 Rename the columns to something cleaner
mpg = mpg.rename(columns = {'cty':'city', 'hwy':'highway', 'cyl':'cylinder', 'drv':'drive'})

#9 Display the summary statistics
# convert highway and city mpg to intergers
mpg['city'] = pd.to_numeric(mpg['city'])
mpg['highway'] = pd.to_numeric(mpg['highway'])
mpg.describe(include = 'all')
'''
                manufacturer	model	displ	year	cylinder	trans	drive	city	highway	fl	   class
count	        234	            234	    234     234 	234         234	    234	    234 	234 	234	    234
unique	        15	            38	    NaN	    NaN	    NaN	        10	    3	    NaN 	NaN	    5	    7
top	            dodge	        caravan2wd      NaN 	NaN	        auto(l4 f	    NaN	    NaN	    r	    suv
freq	        37	            11	    NaN	    NaN	    NaN	        83	    106	    NaN	    NaN	    168	    62
mean	        NaN	            NaN	   3.471795	2003.5	5.888889	NaN	    NaN	    16.858  23.440171	NaN	NaN
std	            NaN	NaN	1.291959	    4.509646	    1.6115  NaN	NaN	            4.2559  5.9546  NaN	    NaN
min	            NaN	            NaN	    1.60000 1999.0  4.0000  NaN	            9.000000	12.000000	NaN	NaN
25%	            NaN	            NaN	    2.40000 1999.0  4.00000 NaN	NaN	        14.000000	18.000000	NaN	NaN
50%	            NaN	            NaN	    3.3000  2003.5  6.0000  NaN	NaN	        17.000000	24.000000	NaN	NaN
75%	            NaN	            NaN	    4.6000  2008.0  8.000   NaN	NaN	        19.000000	27.000000	NaN	NaN
max	            NaN	            NaN	    7.000   2008.00 8.00000 NaN	NaN	        35.000000	44.000000	NaN	NaN
'''
#10
len(mpg['manufacturer'].unique())
mpg['manufacturer'].nunique()
    # 15 unique manufacturers

#11 How many different models are there
len(mpg['model'].unique())
mpg['model'].nunique()
    # 38 unique models

#12 Create a column named mileage difference.
mpg['mileage_difference']= mpg['highway'] - mpg['city']

mpg['mileage_difference'] = mpg['highway'].sub(mpg['city'], axis = 0)
#13 Create a column named average mileage
mpg['average_mileage'] =  (mpg['highway'] + mpg['city']) /2

#   here's a second solution using .mean 
mpg['average_mileage'] = mpg[['highway','city']].mean(axis = 1)
#14 Create a new column named is_automatic that holds bools
mpg['is_automatic'] = np.where(mpg.trans.str.count('auto'), True, False)

# also works 
mpg['is_automatic'] = np.where(mpg.trans.str.contains('auto'), True, False)

# check data type
    mpg.info()

#15
mpg.groupby('manufacturer').average_mileage.agg('mean').sort_values(ascending = False)
'''
manufacturer
honda         28.500000
volkswagen    25.074074
hyundai       22.750000
subaru        22.428571
audi          22.027778
toyota        21.720588
pontiac       21.700000
nissan        21.346154
chevrolet     18.447368
ford          16.680000
mercury       15.625000
jeep          15.562500
dodge         15.540541
lincoln       14.166667
land rover    14.000000
Name: average_mileage, dtype: float64
'''

#16 
mpg.groupby('is_automatic').average_mileage.agg('mean')
    # manual cars have better mpg at 22 mpg, autos have 19 mpg

#EXERCISE III
#1. pull and connect to the chipotle database
def get_chip_url(username, password, host):
    db_url = f'mysql+pymysql://{username}:{password}@{host}/chipotle'
    return db_url

orders_df = get_chip_url(username, password, host)

#2. What's the total price for each order
orders_df['item_price'] = orders_df['item_price'].str.replace('$','').astype(float)\
# most expensive item is at 44 dollars
    #oops, heres the most expensive order total
    order_id = orders_df.groupby('order_id').sum('item_price')
    order_id.max()
    '''
    id            53268.00
    quantity         35.00
    item_price      205.25
    dtype: float64
    '''

#3 What are the 3 most popular items?
quantity = orders_df.groupby('item_name').sum('quantity').sort_values(by= 'quantity', ascending = False).head(3)
'''
                    id	        order_id	quantity	item_price
item_name				
Chicken Bowl	    1780635	    713926	    761	        7342.73
Chicken Burrito	    1238770	    497303	    591	        5575.82
Chips and Guacamole	1122252	    449959	    506	        2201.04
'''

#4 What item has produced the most revenue
total_rev = orders_df.groupby('item_name').sum('item_price').sort_values(by = 'item_price', ascending = False).head(1)
    # Chicken bowl with 761 units sold and an item_price of 7342.73

#5 using the titles dataframe, visualize the number of employees with each title
titles.value_counts('title')
'''
title
Engineer              115003
Staff                 107391
Senior Engineer        97750
Senior Staff           92853
Technique Leader       15159
Assistant Engineer     15128
Manager                   24
dtype: int64
'''

#6 Join employees and titles together
et_df = employees.merge(titles, how='inner', on = 'emp_no', indicator=True)

#7 isualize how frequently employees change titles
tab=pd.crosstab(et_df.emp_no, et_df.title, margins = True)
tab['All'] = (tab['All']-tab['All'].mean())/tab['All'].std()


title_count = et_df.groupby('emp_no').title.count().value_counts()
'''
1    159754
2    137256
3      3014
Name: title, dtype: int64
'''

#8 For each title, find the hire date of the employee that was hired most recently with that title
et_df.groupby('title').hire_date.max()
'''
title
Assistant Engineer    1999-12-24
Engineer              2000-01-28
Manager               1992-02-05
Senior Engineer       2000-01-01
Senior Staff          2000-01-13
Staff                 2000-01-12
Technique Leader      1999-12-31
Name: hire_date, dtype: object
'''

#9 write the code necessary to create a cross tabulation fo the number of titles by department
td = '''SELECT * FROM departments 
            JOIN dept_emp USING(dept_no) 
            JOIN titles using(emp_no) 
            WHERE dept_emp.to_date > curdate() 
            AND titles.to_date > curdate()'''
td_df = pd.read_sql(td, url)
pd.crosstab(td_df.dept_name, td_df.title)
'''
title	            Assistant Engineer	Engineer	Manager	 Senior Engineer	Senior Staff	Staff	Technique Leader
dept_name							
Customer Service	68	                627	        1	    1790	            11268	        3574	241
Development	        1652	            14040	    1	    38816	            1085	        315	    5477
Finance	            0	                0	        1	    0	                9545	        2891	0
Human Resources	    0	                0	        1	    0	                9824	        3073	0
Marketing	        0	                0	        1	    0	                11290	        3551	0
Production	        1402	            12081	    1	    33625	            1123	        349 	4723
Quality Management	389	                3405	    1	    9458	            0	            0	    1293
Research	        77	                830	        1	    2250	            9092	        2870	321
Sales	            0	                0	        1	    0	                28797	        8903	0
'''