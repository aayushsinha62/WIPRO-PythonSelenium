# DataFrame is a 2-dimensional labeled data structure (rows & columns),
# like an Excel SQL tables

import pandas as pd

# Create DataFrame from List of Dictionaries
data = [
    {"Name": "Ram", "Age": 25},
    {"Name": "Sam", "Age": 30},
    {"Name": "John", "Age": 28}
]

df = pd.DataFrame(data)

print(df)

# Create DataFrame from Dictionary of Series


s1 = pd.Series([1, 2, 3])
s2 = pd.Series([4, 5, 6])

df = pd.DataFrame({"A": s1, "B": s2})

print(df)

# Create DataFrame from NumPy Array

import numpy as np


arr = np.array([[1, 2], [3, 4], [5, 6]])
df = pd.DataFrame(arr, columns=["A", "B"])

print(df)

#create dataframe using CSV file

import pandas as pd

df = pd.read_csv("data.csv")

print(df)

#create empty dataframe

df=pd.DataFrame()
print(df)

#create dataframe with custom index

# Create DataFrame with Custom Index

import pandas as pd

data = {
    "Name": ["Ram", "Sam"],
    "Age": [25, 30]
}

df = pd.DataFrame(data, index=["Emp1", "Emp2"])

print(df)