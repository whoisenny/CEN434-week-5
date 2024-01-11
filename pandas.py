import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 28, 22],
    'Score': [85, 70, 90, 80, 75]
}
df = pd.DataFrame(data)

# Displaying basic DataFrame information
print("DataFrame:")
print(df)
print("\nDataFrame Info:")
print(df.info())
print("\nDataFrame Description:")
print(df.describe())

# Indexing and selecting data
print("\nSelecting Columns:")
print(df['Name'])  # Selecting a single column
print("\nSelecting Rows:")
print(df.iloc[2])  # Selecting a single row by index
print("\nSelecting Subset of Data:")
print(df.loc[1:3, ['Name', 'Score']])  # Selecting a subset of rows and columns

# Filtering data
print("\nFiltering Data:")
print(df[df['Age'] > 25])  # Filtering based on condition

# Sorting
print("\nSorting Data:")
print(df.sort_values(by='Age', ascending=False))  # Sorting by Age in descending order

# Adding and deleting columns
df['Grade'] = ['A', 'B', 'A', 'B', 'B']  # Adding a new column
print("\nDataFrame with New Column:")
print(df)
df = df.drop(columns='Grade')  # Deleting the 'Grade' column
print("\nDataFrame with Deleted Column:")
print(df)

# Reading from and writing to CSV file
df.to_csv('sample_data.csv', index=False)  # Writing DataFrame to CSV
new_df = pd.read_csv('sample_data.csv')  # Reading CSV file into a new DataFrame
print("\nNew DataFrame from CSV:")
print(new_df)