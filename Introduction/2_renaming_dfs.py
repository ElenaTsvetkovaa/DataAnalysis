import pandas as pd

df = pd.DataFrame({
    'First Name': ['Elena', 'Maria'],
    'Last Name': ['Ivanova', 'Petrova'],
    'Age': [19, 21]
}, index=['a', 'b'])



print(df)


# Rename columns
columns_mapper = {
    'First Name': 'first_name',
    'Last Name': 'last_name',
    'Age': 'age'}
index_mapper = {
    'a': 'student1',
    'b': 'student2'
}

df.rename(mapper=columns_mapper, axis=1, inplace=True)
df.rename(mapper=index_mapper, axis=0, inplace=True)
print(df)


