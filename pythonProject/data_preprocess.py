import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
import pylab as pl
from sklearn.preprocessing import MinMaxScaler
from data_loader import data_loader
import seaborn as sns


# Preprocess the data
def data_preprocess(data_load):
    # Data Cleaning - Check to see if the dataset has any missing or "null" values. If there are blanks, you can either
    #                 get rid of them or fill them in with the right value. Take out any data points that are repeated.

    if data_load.isnull().sum().sum() > 0:  # checks for null or missing values and counts the missing values, and
        #                                     compares the result to 0.
        print(f"Warning: {data_load.isnull().sum().sum()} missing values.")
        data_load.fillna(data_load.mean(), inplace=True)  # Use the average of the feature to fill in the missing values
    else:
        print("No missing values.")

    if data_load.duplicated().sum() > 0:  # count the total number of duplicated rows in the entire dataset.
        print(f"Warning: {data_load.duplicated().sum()} duplicates")
        data_load.drop_duplicates(inplace=True)  # remove duplicates
    else:
        print("No duplicate values")

    plt.scatter(data_load['Age'], data_load['HeartDisease'])  # create a scatter plot
    plt.xlabel('Age')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship')
    plt.show()

    disease_by_sex = data.groupby(['Sex', 'HeartDisease']).size().unstack()  # Count the incidences by Sex and
    #                                                                          HeartDisease.
    disease_by_sex.plot(kind='bar', stacked=True)  # create a stacked bar chart
    plt.xlabel('Heart Disease')
    plt.ylabel('Number of Patients')
    plt.title('Relationship')
    plt.show()

    disease_by_cpt = data_load.groupby('ChestPainType')['HeartDisease'].sum()
    plt.bar(disease_by_cpt.index, disease_by_cpt.values)  # bar chart
    plt.xlabel('Chest Pain Type')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship')
    plt.show()

    plt.scatter(data_load['RestingBP'], data_load['HeartDisease'])
    plt.xlabel('Resting blood pressure')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship')
    plt.show()

    plt.scatter(data_load['Cholesterol'], data_load['HeartDisease'])
    plt.xlabel('Cholesterol')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship')
    plt.show()

    sns.countplot(x='FastingBS', hue='HeartDisease', data=data)
    plt.xlabel('Fasting Blood Sugar (mg/dL)')
    plt.ylabel('Number of Patients')
    plt.title('Heart Disease Patients by Fasting Blood Sugar Level')
    plt.show()

    resting_ecg_counts = data_load['RestingECG'].value_counts()
    disease_by_resting_ecg = data_load.groupby('RestingECG')['HeartDisease'].sum()
    plt.bar(resting_ecg_counts.index, disease_by_resting_ecg)
    plt.xlabel('Resting Electrocardiogram Result')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('HeartDisease by RestingECG')
    plt.show()

    plt.scatter(data_load['MaxHR'], data_load['HeartDisease'])
    plt.xlabel('maximum heart rate')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship between MaxHR and HeartDisease')
    plt.show()

    disease_by_ea = data_load.groupby(['ExerciseAngina', 'HeartDisease'])['HeartDisease'].count()
    disease_by_ea.unstack().plot(kind='bar', stacked=True)
    plt.xlabel('Exercise-induced angina')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Heart Disease and Exercise Angina')
    plt.show()



data, info_str = data_loader()
data_preprocess(data)

'''


    # Data Scaling - Make sure that all the features are the same size by putting them on the same scale.
    #

    scaler = MinMaxScaler()  # scale the numerical columns of the dataset to the same range.
    cols = data_load.select_dtypes(include='number').columns.tolist()  # Pick just numerical dataset columns by
    #                                                                    checking for numerical data types and saving
    #                                                                    their column names in a list.
    data_load[cols] = scaler.fit_transform(data_load[cols])  # identify the numerical and category columns

    # create a figure with subplots for each column
    fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(20, 15))

    # loop over each column and plot a histogram
    for i, col in enumerate(df.columns):
        ax = axs[i // 4, i % 4]  # select the appropriate subplot
        ax.hist(df[col], bins=20, color='blue', alpha=0.5)  # plot histogram
        ax.set_title(col)  # set the subplot title

    # adjust the spacing between subplots

    plt.tight_layout()

    # show the plot
    plt.show()

    # Data Encoding - If the dataset has categorical features, like gender or type of disease, you should turn them into
    #                 numbers that the model can use.

    # Data Features - Choose the most important features for the machine learning model and get rid of any features that
    #                 are redundant or don't matter.

    # Train-Test Split - Break up the data into sets for training, validating, and testing.


data, info_str = data_loader()
data_preprocess(data)


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
print('Number of ST:', count_st')
'''
