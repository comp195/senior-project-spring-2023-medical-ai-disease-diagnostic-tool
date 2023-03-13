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
