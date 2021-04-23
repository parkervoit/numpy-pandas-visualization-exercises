from pydataset import data
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

iris_df = sns.load_dataset('iris')
# Part 1
# 1. What does the distribution of petal lengths look like?
sns.displot(iris_df['Petal.Length'], color = 'b', kde = True, edgecolor = 'b')
    # distribution is left skewed 

# 2. Is there a correlation between petal length and petal width?
sns.heatmap(iris_df.corr(), cmap = 'coolwarm_r', annot = True, vmax = 1, vmin = -1)
    # this gives a heatmap, coolwarm_r for visual clarity

sns.regplot(data = iris_df, x = 'petal_length',y = 'petal_width')
    # Scatter regplot to show CI and fit line

sns.relplot(data = iris_df, x = 'petal_length',y = 'petal_width', hue = 'species')
    # this scatter has it seperated out by species

#from visual inspection, there is a correlation

#3. Would it be reasonable to predict species based on sepal width and sepal length?
sns.relplot(data = iris_df, x = 'sepal_length',y = 'sepal_width', hue = 'species')
    # not completely reasonable. While there is still clustering going on, there is 
    # too much overlap between two species to give a better answer than 
    # "its probably one of these two species"

#4 Which features would be best used to predict species?
sns.relplot(data = iris_df, x = 'petal_length',y = 'petal_width', hue = 'species')
    # petal length or width, species are very nicely clustered when comparing those values


#Part Deux
#1. 
ans_df = sns.load_dataset('anscombe')
'''
	x	y
count	mean	std	min	25%	50%	75%	max	count	mean	std	min	25%	50%	75%	max
dataset																
I	11.0	9.0	3.316625	4.0	6.5	9.0	11.5	14.0	11.0	7.500909	2.031568	4.26	6.315	7.58	8.57	10.84
II	11.0	9.0	3.316625	4.0	6.5	9.0	11.5	14.0	11.0	7.500909	2.031657	3.10	6.695	8.14	8.95	9.26
III	11.0	9.0	3.316625	4.0	6.5	9.0	11.5	14.0	11.0	7.500000	2.030424	5.39	6.250	7.11	7.98	12.74
IV	11.0	9.0	3.316625	8.0	8.0	8.0	8.0	19.0	11.0	7.500909	2.030579	5.25	6.170	7.04	8.19	12.50
'''
    # the x values all share the the same counts, means, stds, but different counts, and percentile values.
    # the y values are drastically different, so you would expect different graphs

sns.lmplot(data = ans_df, x = 'x', y = 'y', col = 'dataset', truncate = False)

#2. Create a boxplot that shows the effectiveness of different insect sprays
sns.relpot(data = ans_df, x = 'x', y = 'y', col = 'dataset')

#3. 
swiss_df = data('swiss')
# a.Create an attribute named is_catholic that holds a boolean value
swiss_df['is_catholic'] = swiss_df['Catholic'] > 75
#b
sns.lmplot(data = swiss_df, x = 'Catholic', y = 'Fertility')
    # there seems to be a weak positive correlation between the two
sns.boxplot(data = swiss_df, x = 'is_catholic', y = 'Fertility')
    # IQRs of both box plots don't overlap, so probably correlated

# We can also test it statistically with an unpaired t test using the scipy library

#First, check to see if thier variance is equal with Levene's test
sp.stats.levene(catholics_df['Fertility'], noncat_df['Fertility'])
    # LeveneResult(statistic=0.36861426253423696, pvalue=0.5468120297876446)
    # The p value suggests that the groups' variances are not statistically different
    # this means that we can assume homogeniety between both sample populations

# Group data by whether or not they are catholic, creating a boolean mask and then applying it to create a new df
catholics_df = swiss_df[swiss_df['is_catholic'] == True]
noncat_df = swiss_df[swiss_df['is_catholic'] == False]

# Run the ttest, pulling only from the fertility columns, set equal_var to true since our levenes was not
# statistically significant. 
sp.stats.ttest_ind(catholics_df['Fertility'], noncat_df['Fertility'] , equal_var=True)
      #Ttest_indResult(statistic=5.09743444515206, pvalue=6.645861971829059e-06)
      # this suggests that the fertility rate between catholics and non catholics is strongly significant

#c What measure correlates most strongly with fertility?
sns.heatmap(swiss_df.corr(), cmap = 'coolwarm_r', annot = True, vmax = 1, vmin = -1)
    # education and examination

#4. Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each. 
# import login info and import function
from env import host, username, password
def get_db_url(username,password,host,db_name):
    return f'mysql+pymysql://{username}:{password}@{host}/{db_name}'

# use function to call information
chip_url = get_db_url(username,password,host, 'chipotle')
# import chipotle orders table and save as variable
orders_df = pd.read_sql('select * from orders', chip_url)
# clean up value types to do math on price
orders_df.item_price = orders_df.item_price.str.replace('$','').str.replace(',','').astype('float')
# create new dataframe that pulls out the 4 top selling items and their quantity
top_df = orders_df.groupby('item_name')[['quantity', 'item_price']].sum().sort_values(by = 'quantity', ascending = False).head(4)

# plot as a bar plot to see the total amount sold
sns.barplot(data = top_df, x = ['Chicken Bowl','Chicken Burrito','Chips and Guac','Steak Burrito'], y = 'item_price')

#5 Load the sleepstudy data and read ists documentation. Use seaborn to create a line chart of all the individuals
# reaction times and more prominant line showing average change in reaction time

#load data and check docs
sleep_df = data('sleepstudy')
data('sleepstudy', show_doc= True)

# create figure to write to
plt.figure(figsize = (20,10))

# plot sleep_df data and also mean line using estimator. Make mean line transparent and thick to improve readability
sns.lineplot(data = sleep_df, x = 'Days', y = 'Reaction', 
            hue = 'Subject', legend = 'full',
            palette = 'pastel', linewidth = 3)
sns.lineplot(data = sleep_df, x = 'Days', y = 'Reaction', 
             color = 'blue', linewidth = 10, estimator = 'mean', alpha =.4)

# add a legend 
plt.legend(loc = 'upper left', fontsize = 'large')

# format title, ticks, and labels
plt.title('Reaction Times in a Sleep Deprivation Study', fontsize = 20)
plt.xticks(fontsize = 15)
plt.yticks(fontsize = 15)
plt.ylabel('Reaction', fontsize = 15)
plt.xlabel('Days', fontsize = 15)