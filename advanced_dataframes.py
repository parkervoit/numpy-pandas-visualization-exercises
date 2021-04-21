#1 Create a function named get_db_url. It should accept a username, hostname, password, 
# and database name and return a url connection string formatted like in the example at the start of this lesson.
from env import host, user, password
import pandas as pd 

from env import host, username, password
import pandas as pd
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