import pandas as pd

# Open the CSV file for reading
with open('heart.csv', 'r') as f:

    # Read lines from file
    lines = f.readlines()

    # Remove newline characters from lines
    lines = [line.strip() for line in lines]

    # Split lines into fields
    fields = [line.split(';') for line in lines]

# Create a pandas DataFrame from the fields
df = pd.DataFrame(fields[1:], columns=fields[0])

# Convert columns to numeric data types
df['Age'] = pd.to_numeric(df['Age'])
df['RestingBP'] = pd.to_numeric(df['RestingBP'])
df['Cholesterol'] = pd.to_numeric(df['Cholesterol'])
df['FastingBS'] = pd.to_numeric(df['FastingBS'])
df['RestingECG'] = pd.to_numeric(df['RestingECG'])
df['MaxHR'] = pd.to_numeric(df['MaxHR'])
df['ExerciseAngina'] = pd.to_numeric(df['ExerciseAngina'])
df['Oldpeak'] = pd.to_numeric(df['Oldpeak'])
df['ST_Slope'] = pd.to_numeric(df['ST_Slope'])
df['HeartDisease'] = pd.to_numeric(df['HeartDisease'])

# Sort the DataFrame by the 'Age' column
sorted_df = df.sort_values(by='Age')

# Identify the high and low values for the 'Cholesterol' column
low_value = sorted_df['Cholesterol'].min()
high_value = sorted_df['Cholesterol'].max()

# Identify the number of 'normal' and 'ST' values in the 'ST_Slope' column
count_normal = sorted_df[sorted_df['ST_Slope'] == 1].shape[0]
count_st = sorted_df[sorted_df['ST_Slope'] == 2].shape[0]

# Loop through every value in the sorted DataFrame and print it
for index, row in sorted_df.iterrows():
    for col in sorted_df.columns:
        print(row[col])

print('Lowest Cholesterol:', low_value)
print('Highest Cholesterol:', high_value)
print('Number of normal:', count_normal)
print('Number of ST:', count_st)

