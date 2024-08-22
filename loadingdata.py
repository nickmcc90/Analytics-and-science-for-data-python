import pandas as pd
import numpy as np

import sqlite3

# reading csv file
data_csv = pd.read_csv('filename.csv')

# reading txt file
data_txt = pd.read_txt('textfile', header = 0, sep = ',')

# reading excel file
data_excel = pd.read_excel('textfile', header = 0, sep = ',')

# reading json file
data_json = pd.read_json('textfile', header = 0, sep = ',')

# connection to sql database
connection_db = sqlite3.connect("database_name.db")
query_1 = 'SELECT col_1 FROM table_name'

data_sql = pd.read_sql(query_1, connection_db)


# pretend that data is a data frame.
data = {}
data.sort_values(by = 'Salary', ascending=True)

# this is the number of times each department appears for the other columns
data.groupby("Department").count()
# and this is how many times each department appears for the name column only
data.groupby("Department")["Name"].count()

# let's grab the average salary per department
data.groupby("Department")["Salary"].mean()
# this grabs the lease salary per department
data.groupby("Department")["Salary"].mean()

# if we want to display a certain salary above 100k, we do it this way..
data[data["Salary"] > 100000]

# If we want to include a range of salaries to print, we can do this:
data[data["Salary"] > 100000 and data["Salary"] < 200000]

# If we want a specific value, we use isin()
data[data["Age"].isin([20,65])]


######DESCRIPTIVE STATISTICS
data2 = [100, 30, 44, 54, 66, 73, 35, 32]
mean = np.mean(data2)
median = np.median(data2)

from scipy import stats
mode = stats.mode(data2)

variance = np.var(data2)
std = np.std(data2)

print(data2.describe())