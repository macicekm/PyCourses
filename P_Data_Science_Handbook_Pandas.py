import numpy as np
import pandas as pd


########################################################################################################################
# Pandas Series Object

data = pd.Series([0.25, 0.5, 0.75, 1.0])

print(data)

print(data.values)

print(data.index)

print(data[1])

print(data[1:3])


data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

print(data['b'])


population_dict = {'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}

population = pd.Series(population_dict)

print(population)


print(population['California':'New York'])


########################################################################################################################
# Pandas DataFrame Object


area_dict = {'California': 423967, 'Texas': 695662, 'New York': 141297,
'Florida': 170312, 'Illinois': 149995}

area = pd.Series(area_dict)

# Creating a dataframe from two series, which vere originally created as a dictionary
states = pd.DataFrame({'population': population, 'area': area})

print(states.index)
print(states.columns)

print(states['area'])

########################################################################################################################
# Data Selection in Series
data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])

print(data.keys())

data['e'] = 1.25

# slicing by explicit index
data['a':'c']

# slicing by implicit integer index
data[0:2]

# masking
data[(data > 0.3) & (data < 0.8)]

# fancy indexing
data[['a', 'e']]


# Indexers: loc, iloc, and ix

data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])

#loc attribute allows indexing and slicing that always references the explicit

data.loc[1]
data.loc[1:3]

#iloc attribute allows indexing and slicing that always references the implicit Python-style index
data.iloc[1]
data.iloc[1:3] # begins from 0

# explicit is better than implicit.”

########################################################################################################################
# Data Selection in DataFrame