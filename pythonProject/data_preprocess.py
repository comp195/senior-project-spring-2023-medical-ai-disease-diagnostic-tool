import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from sklearn.preprocessing import MinMaxScaler
from data_loader import data_loader
import seaborn as sns


# Preprocess the data
def data_preprocess(data_load):
    # Data Cleaning - remove mistakes, inconsistencies, and missing values using imputation, outlier identification,
    #                 and data deduplication.

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

    #       Visualization of correlation between variables and target variable

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

    plt.scatter(data_load['Oldpeak'], data_load['HeartDisease'], c=data_load['HeartDisease'])
    plt.xlabel('Exercise-induced ST depression')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Oldpeak-HeartDisease Connection')
    plt.show()

    disease_by_sts = data_load.groupby(['ST_Slope', 'HeartDisease']).size().unstack()
    disease_by_sts.plot(kind='bar', stacked=True)
    plt.xlabel('ST segment slope')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship')
    plt.show()

    corr_matrix = data_load.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
    plt.show()

    #       visualization of distribution of variables

    age_data = data_load['Age']
    sns.histplot(age_data, kde=False)  # create histogram
    plt.title('Distribution of Ages')
    plt.xlabel('Age')
    plt.ylabel('Number of Patents')
    plt.show()

    sex_data = data_load['Sex']
    sns.histplot(sex_data, kde=False)
    plt.title('Distribution of Sex')
    plt.xlabel('Sex')
    plt.ylabel('Number of Patients')
    plt.show()

    cpt_data = data_load['ChestPainType']
    sns.histplot(cpt_data, kde=False)
    plt.title('Distribution of Chest Pain Types')
    plt.xlabel('Chest Pain Type')
    plt.ylabel('Number of Patients')
    plt.show()

    rbp_data = data_load['RestingBP']
    sns.histplot(rbp_data, kde=False)
    plt.title('Distribution of Resting Blood Pressures')
    plt.xlabel('Resting Blood Pressure')
    plt.ylabel('Number of Patients')
    plt.show()

    chol_data = data_load['Cholesterol']
    sns.histplot(chol_data, kde=False)
    plt.title('Distribution of Cholesterol')
    plt.xlabel('Cholesterol')
    plt.ylabel('Number of Patients')
    plt.show()

    fbs_data = data_load['FastingBS']
    sns.histplot(fbs_data, kde=False)
    plt.title('Distribution of Fasting Blood Pressures')
    plt.xlabel('Fasting Blood Pressure')
    plt.ylabel('Number of Patients')
    plt.show()

    recg_data = data_load['RestingECG']
    sns.histplot(recg_data, kde=False)
    plt.title('Distribution of Resting Electrocardiograms')
    plt.xlabel('Resting Electrocardiograms')
    plt.ylabel('Number of Patients')
    plt.show()

    mhr_data = data_load['MaxHR']
    sns.histplot(mhr_data, kde=False)
    plt.title('Distribution of Maximum Heart Rates')
    plt.xlabel('Maximum Heart Rates')
    plt.ylabel('Number of Patients')
    plt.show()

    ea_data = data_load['ExerciseAngina']
    sns.histplot(ea_data, kde=False)
    plt.title('Distribution of Exercise-induced angina')
    plt.xlabel('Exercise-induced angina')
    plt.ylabel('Number of Patients')
    plt.show()

    op_data = data_load['Oldpeak']
    sns.histplot(op_data, kde=False)
    plt.title('Distribution of Exercise-induced ST depressions')
    plt.xlabel('Exercise-induced ST depressions')
    plt.ylabel('Number of Patients')
    plt.show()

    sts_data = data_load['ST_Slope']
    sns.histplot(sts_data, kde=False)
    plt.title('Distribution of ST segment slope')
    plt.xlabel('ST segment slope')
    plt.ylabel('Number of Patients')
    plt.show()

    #       Data Scaling - Make sure that all the features are the same size by putting them on the same scale.
    #                      to make sure that high-value features don't take over the model and skew the results.

    scaler = MinMaxScaler()  # scale the numerical columns of the dataset to the same range.
    cols = data_load.select_dtypes(include='number').columns.tolist()  # Pick just numerical dataset columns by
    #                                                                    checking for numerical data types and saving
    #                                                                    their column names in a list.
    data_load[cols] = scaler.fit_transform(data_load[cols])  # identify the numerical and category columns

    #       Data Encoding - If the dataset has categorical features, like gender or type of disease, you should turn them
    #                       into numbers that the model can use.


data, info_str = data_loader()
data_preprocess(data)

'''

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
