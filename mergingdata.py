# Here we will look at merging and joins

import pandas as pd

# Creating two dataframes
data1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D', 'E', 'F'], 'value': [1, 2, 3, 4, 5, 6, 7]})

data2 = pd.DataFrame({'key': ['C', 'D', 'E', 'F', 'G', 'H'], 'value': [8, 9, 10, 11, 12, 13, 14]})