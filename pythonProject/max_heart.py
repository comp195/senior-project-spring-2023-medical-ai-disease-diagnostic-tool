import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# load data from csv file
df = pd.read_csv('heart.csv')

# create a color map based on the Age column
age_cmap = plt.get_cmap('cool')(np.linspace(0, 1, len(df['Age'].unique())))

# create scatter plot for RestingBP and Cholesterol, color-coded by Age
plt.scatter(df['RestingBP'], df['Cholesterol'], c=age_cmap[df['Age'].astype('category').cat.codes])
plt.title('Resting Blood Pressure vs Cholesterol')
plt.xlabel('Resting Blood Pressure')
plt.ylabel('Cholesterol')
plt.show()

# create a color map based on the Sex column
sex_cmap = plt.get_cmap('coolwarm')(np.linspace(0, 1, len(df['Sex'].unique())))

# create scatter plot for MaxHR and Age, color-coded by Sex
plt.scatter(df['MaxHR'], df['Age'], c=sex_cmap[df['Sex'].astype('category').cat.codes])
plt.title('Maximum Heart Rate vs Age')
plt.xlabel('Maximum Heart Rate')
plt.ylabel('Age')
plt.show()

# create a color map based on the HeartDisease column
hd_cmap = plt.get_cmap('Set1')(np.linspace(0, 1, len(df['HeartDisease'].unique())))

# create scatter plot for Oldpeak and MaxHR, color-coded by HeartDisease
plt.scatter(df['Oldpeak'], df['MaxHR'], c=hd_cmap[df['HeartDisease']])
plt.title('ST Depression vs Maximum Heart Rate')
plt.xlabel('ST Depression')
plt.ylabel('Maximum Heart Rate')
plt.show()

# New code 04/7/2023)

df = pd.read_csv('heart.csv')

# Define the column names and titles for each histogram
columns = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
           'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'HeartDisease']

titles = ['Age Distribution' , 'Sex Distribution' , 'Chest Pain Type Distribution' ,
          'Resting Blood Pressure Distribution', 'Cholesterol Distribution',
          'Fasting Blood Sugar Distribution', 'Resting Electrocardiogram Distribution',
          'Maximum Heart Rate Distribution', 'Exercise-Induced Angina Distribution',
          'ST Depression Distribution', 'ST Slope Distribution', 'Heart Disease Distribution']

# Create a figure with 4 rows and 3 columns of subplots
fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(12, 16))

# Plot each histogram in a separate subplot
for i, ax in enumerate(axs.flat):
    if i < len(columns):
        ax.hist(df[columns[i]])
        ax.set_title(titles[i])
        ax.set_xlabel(columns[i])
        ax.set_ylabel('Frequency')

# Adjust the spacing between subplots to avoid title overlapping
plt.subplots_adjust(top=0.92, hspace=0.4, wspace=0.4)

# Display the figure
plt.show()


# read the CSV file
df = pd.read_csv('heart.csv')

# calculate the correlation matrix
corr_matrix = df.corr()

# display the correlation matrix
print(corr_matrix)

# select the most highly correlated features
most_correlated = corr_matrix.nlargest(10, 'target')['target'].index

# display the most highly correlated features
print(most_correlated)
