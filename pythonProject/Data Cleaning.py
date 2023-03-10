import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('heart.csv')

# Sort the DataFrame by the 'age' column
sorted_df = df.sort_values(by='age')

# Display the first few rows of the sorted DataFrame
print(sorted_df.head())

