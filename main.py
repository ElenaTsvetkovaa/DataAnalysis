import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({
    'Name': ['Steve', 'Lia', 'Vin', 'Katie'],
    'Age': [32, 28, 45, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female'],
    'Rating': [3.45, 4.6, 3.9, 2.78]},
    index=['r1', 'r2', 'r3', 'r4'])

# Display the Input DataFrame
print('Input DataFrame:\n', df)

# Modify the Row labels of the DataFrame
df.index = [100, 200, 300, 400]
print('Output Modified DataFrame with the updated index labels:\n', df)


df.columns = ['IME', 'GODINI', 'POL', 'STEP']
print('Modified columns df:\n', df)


