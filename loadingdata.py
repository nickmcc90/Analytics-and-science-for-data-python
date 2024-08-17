import pandas as pd

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
data.sort_values