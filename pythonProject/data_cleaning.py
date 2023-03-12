import pandas as pd
import numpy as np
import csv


# Open the CSV file for reading

d = pd.read_csv('heart.csv')
print(d.values)

d.loc[:,"Age"]
print(d.loc[:,"Age"])

with open('heart.csv', 'r') as f:

    # Read lines from file
    lines = f.readlines()

    # Remove newline characters from lines
    lines = [line.strip() for line in lines]

    # Split lines into fields
    fields = [line.split(';') for line in lines]

# Create a pandas DataFrame from the fields
df = pd.read_csv('heart.csv')
print(df)

# Convert columns to numeric data types
Age = df.loc[:,'Age']
print(Age)

RestingBP = df.loc[:,'RestingBP']
print(RestingBP)

Cholesterol = df.loc[:,'Cholesterol']
print(Cholesterol)

FastingBS = df.loc[:,'FastingBS']
print(FastingBS)

RestingECG = df.loc[:,'RestingECG']
print(RestingECG)

MaxHR= df.loc[:,'MaxHR']
print(MaxHR)

ExerciseAngina= df.loc[:,'ExerciseAngina']
print(ExerciseAngina)

Oldpeak = df.loc[:,'Oldpeak']
print(Oldpeak)

ST_Slope = df.loc[:,'ST_Slope']
print(ST_Slope)

HeartDisease = df.loc[:,'HeartDisease']
print(HeartDisease)


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

