import pandas as pd


# This will create the data frame object, much like a data table in form.
# These are key-value pairs in a sense, making objects in a table using the lists given.
# Creating Data Frames from a Dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [16, 21, 27]
}

df = pd.DataFrame(data)

print(df)


# Reading Data from Files
# We can read from multiple sources, but CSV is most like our DataFrame objects so it will likely be commonly used.
# csv_df = pd.read_csv('file.csv')


# Basic Operations ------------------------------------------------------------------

# Viewing Data
print(df.head()) # First 5 Rows of the Table
print(df.info()) # Gives back a summarized version of the Dataframe

# Selecting Columns
ages = df['Age'] # Much like a dictionary, we can use this setup to retrieve a specific column or set of data. Much like an SQL Query.

# Filtering Rows
adults = df[df['Age'] >= 18] # Treat this like an SQL Query in a sense. We would return rows where the Age value is equal to or above 18.


# Data Manipulation ----------------------------------------------------------------

# Adding a new Column
df['Is_Adult'] = df['Age'] >= 18
print(df)

# Removing a Column
df.drop('Is_Adult', axis=1, inplace=True)

# Group By; Much like an SQL Query
age_counts = df.groupby('Age').count()
print(age_counts)