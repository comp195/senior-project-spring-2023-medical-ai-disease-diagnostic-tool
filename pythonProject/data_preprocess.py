import pandas as pd
import numpy as np
import csv

# Import dataLoader function from dataLoader file
from data_loader import data_loader


# Preprocess the data
def data_preprocess(data):
    data = data.drop_duplicates()  # check and remove duplicates
    data = data.dropna()  # remove null values


with open('heart.csv', 'r') as f:
    # Read lines from file
    lines = f.readlines()

    # Remove newline characters from lines
    lines = [line.strip() for line in lines]

    # Split lines into fields
    fields = [line.split(';') for line in lines]

# Create a pandas DataFrame from the fields
df = pd.read_csv('heart.csv')

# Convert columns to numeric data types
Age = df.loc[:, 'Age']

RestingBP = df.loc[:, 'RestingBP']

Cholesterol = df.loc[:, 'Cholesterol']

FastingBS = df.loc[:, 'FastingBS']

RestingECG = df.loc[:, 'RestingECG']

MaxHR = df.loc[:, 'MaxHR']

ExerciseAngina = df.loc[:, 'ExerciseAngina']

Oldpeak = df.loc[:, 'Oldpeak']

ST_Slope = df.loc[:, 'ST_Slope']

HeartDisease = df.loc[:, 'HeartDisease']

print(df)

# Sort the DataFrame by the 'Age' column
sorted_df = df.sort_values(by='Age')

# Identify the high and low values for the 'Cholesterol' column
low_value = sorted_df['Cholesterol'].min()
high_value = sorted_df['Cholesterol'].max()

# Identify the number of 'normal' and 'ST' values in the 'ST_Slope' column

count_normal = sorted_df['RestingECG'].value_counts()['Normal']
count_st = sorted_df['RestingECG'].value_counts()['ST']
count_lvh = sorted_df['RestingECG'].value_counts()['LVH']

print('Lowest Cholesterol:', low_value)
print('Highest Cholesterol:', high_value)
print('Number of normal:', count_normal)
print('Number of ST:', count_st)
