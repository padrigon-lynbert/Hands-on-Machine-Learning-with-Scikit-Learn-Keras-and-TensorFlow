import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': ['a', 'b', 'c', 'd', 'e']}
df = pd.DataFrame(data)

# Selecting rows and columns using .iloc[]
# print(df.iloc[0])  # Selects the first row
# print(df.iloc[:, 0])  # Selects the first column
# print(df.iloc[[0, 2], [0, 1]])  # Selects specific rows and columns