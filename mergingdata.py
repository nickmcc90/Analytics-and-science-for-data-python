# Here we will look at merging and joins

import pandas as pd

# Creating two dataframes
data1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], 'value': [1, 2, 3, 4, 5, 6, 7]})

data2 = pd.DataFrame({'key': ['C', 'D', 'E', 'F', 'G', 'H'], 'value': [8, 9, 10, 11, 12, 13]})


# Let's print these frames first
print(data1)
print(data2)

# Let's do an inner join. Shows all matching left and right

merge_inner_join = pd.merge(data1, data2, on='key', how='inner')
print(merge_inner_join)

# Let's do a left join. Shows all data1 and matching data1 and data2. It will show some NaN values
# 2 columns in data2.
merge_left_join = merge_inner_join = pd.merge(data1, data2, on='key', how='left')
print(merge_left_join)

# A right join is the same here.


# Let's do a left anti join.