pip install pandas

##Reading a CSV File:
import pandas as pd

# Reading a CSV file into a DataFrame
data = pd.read_csv('path_to_your_file.csv')

# Display the first few rows of the DataFrame
print(data.head())

##Handling Missing Values:
# Check for missing values
print(data.isnull().sum())

# Fill missing values with a specific value
data_filled = data.fillna(0)

# Drop rows with missing values
data_dropped = data.dropna()

# Replace missing values with the mean of the column
data_mean_filled = data.fillna(data.mean())


##Removing Duplicates:
# Check for duplicate rows
print(data.duplicated().sum())

# Drop duplicate rows
data_no_duplicates = data.drop_duplicates()

# Optionally, keep only the first occurrence of each duplicate
data_no_duplicates = data.drop_duplicates(keep='first')

##Filtering Data:
# Filter rows based on a condition
filtered_data = data[data['column_name'] > value]

# Filter rows based on multiple conditions
filtered_data = data[(data['column_name1'] > value1) & (data['column_name2'] < value2)]


##Sorting Data:
# Sort data by a single column
sorted_data = data.sort_values(by='column_name')

# Sort data by multiple columns
sorted_data = data.sort_values(by=['column_name1', 'column_name2'], ascending=[True, False])

##Grouping Data:
# Group data by a column and calculate the mean of each group
grouped_data = data.groupby('column_name').mean()

# Group data by multiple columns and calculate the sum of each group
grouped_data = data.groupby(['column_name1', 'column_name2']).sum()

# Group data and apply multiple aggregation functions
grouped_data = data.groupby('column_name').agg({'column1': 'sum', 'column2': 'mean'})


##Example Workflow
import pandas as pd

# Read the CSV file
data = pd.read_csv('path_to_your_file.csv')

# Display the first few rows
print("Initial Data:")
print(data.head())

# Handle missing values by filling with the mean
data = data.fillna(data.mean())

# Remove duplicate rows
data = data.drop_duplicates()

# Filter the data where a column value is greater than a specific value
filtered_data = data[data['column_name'] > value]

# Sort the filtered data by a column
sorted_filtered_data = filtered_data.sort_values(by='column_name')

# Group the sorted data by a column and calculate the mean
grouped_data = sorted_filtered_data.groupby('column_name').mean()

# Display the grouped data
print("Grouped Data:")
print(grouped_data)
