import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sns as sns
from scipy.stats import chi2_contingency
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
from seaborn import heatmap


from pythonProject.data_loader import data_loader

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

titles = ['Age Distribution', 'Sex Distribution', 'Chest Pain Type Distribution',
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

print('Convert columns to numeric data types >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

df = pd.read_csv('heart.csv')

# Convert columns to numeric data types
Age = pd.to_numeric(df.loc[:, 'Age'], errors='coerce')
RestingBP = pd.to_numeric(df.loc[:, 'RestingBP'], errors='coerce')
Cholesterol = pd.to_numeric(df.loc[:, 'Cholesterol'], errors='coerce')
FastingBS = pd.to_numeric(df.loc[:, 'FastingBS'], errors='coerce')
RestingECG = pd.to_numeric(df.loc[:, 'RestingECG'], errors='coerce')
MaxHR = pd.to_numeric(df.loc[:, 'MaxHR'], errors='coerce')
ExerciseAngina = pd.to_numeric(df.loc[:, 'ExerciseAngina'], errors='coerce')
Oldpeak = pd.to_numeric(df.loc[:, 'Oldpeak'], errors='coerce')
ST_Slope = pd.to_numeric(df.loc[:, 'ST_Slope'], errors='coerce')
HeartDisease = pd.to_numeric(df.loc[:, 'HeartDisease'], errors='coerce')

# Create a new DataFrame with the updated variables
df_updated = pd.DataFrame({'Age': Age, 'RestingBP': RestingBP, 'Cholesterol': Cholesterol,
                           'FastingBS': FastingBS, 'RestingECG': RestingECG, 'MaxHR': MaxHR,
                           'ExerciseAngina': ExerciseAngina, 'Oldpeak': Oldpeak, 'ST_Slope': ST_Slope,
                           'HeartDisease': HeartDisease})

# Sort the DataFrame by the 'Age' column in ascending order
df_sorted = df_updated.sort_values(by='Age')

# Print the sorted DataFrame
print(df_sorted)

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

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# Convert the 'Age' column to numeric data type
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
# Categorize ages into young, middle-aged, and old
age_categories = pd.cut(df['Age'], bins=[0, 30, 60, 100], labels=['young', 'middle-aged', 'old'])
df['Age Category'] = age_categories
# Select only the numeric columns for the sum
numeric_cols = df.select_dtypes(include=np.number).columns
# Group the DataFrame by the 'Age Category' column and sum the values in each group
age_sum = df.groupby('Age Category')[numeric_cols].sum()
# Print the result
print(age_sum)

print('Chi-Squared Test >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# Load the Heart Disease dataset
df = pd.read_csv('heart.csv')
# Select the categorical or columns features
columns = ['Age', 'Sex', 'ChestPainType', 'RestingBP', 'Cholesterol', 'FastingBS',
           'RestingECG', 'MaxHR', 'ExerciseAngina', 'Oldpeak', 'ST_Slope', 'HeartDisease']
# Loop through all pairs of categorical features and calculate the chi-square statistic and p-value
for i in range(len(columns)):
    for j in range(i + 1, len(columns)):
        contingency_table = pd.crosstab(df[columns[i]], df[columns[j]])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        print(f'Chi-square test between {columns[i]} and {columns[j]}:')
        print(f'    Chi-square statistic = {chi2:.2f}')
        print(f'    p-value = {p:.5f}')
        print(f'    Degrees of freedom = {dof}')

print('Correlation Analysis >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# load the heart disease dataset
df = pd.read_csv('heart.csv')
# calculate the correlation matrix
corr_matrix = df.corr()
# display the correlation matrix
print(corr_matrix)
# select the most highly correlated features
most_correlated = corr_matrix.nlargest(10, 'HeartDisease')['HeartDisease'].index
# display the most highly correlated features
print(most_correlated)

print('Newcorrelationgraph')


# Load data
df = pd.read_csv('heart.csv')

# Calculate the correlation matrix
corr_matrix = df.corr()

# Select the most highly correlated features
most_correlated = corr_matrix.nlargest(10, 'HeartDisease')['HeartDisease'].index

# Create a heatmap of the most highly correlated features
heatmap(df[most_correlated].corr(), annot=True, cmap='coolwarm')


# Display the plot
plt.show()



print('Recursive Feature Elimination >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


# Recursive Feature Elimination:

# Load the dataset
df = pd.read_csv('heart.csv')

# Encode the categorical features using one-hot encoding
df = pd.get_dummies(df, columns=['Sex', 'ChestPainType', 'FastingBS', 'RestingECG', 'ExerciseAngina', 'ST_Slope'])

# Separate the target variable from the features
X = df.drop('HeartDisease', axis=1)
y = df['HeartDisease']

# Create the RFE object and fit it to the data
estimator = LogisticRegression(solver='lbfgs', max_iter=1000)
rfe = RFE(estimator, n_features_to_select=6)
rfe.fit(X, y)

# Print the selected features
print(X.columns[rfe.support_])


print('Bar Chart>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# Define a dictionary to store the associations and their p-values
associations = {
    "Age and Sex": 0.11735,
    "Age and ChestPainType": 0.00002,
    "Age and RestingBP": 0.95938,
    "Age and Cholesterol": 0.04217,
    "Age and FastingBS": 0.13338,
    "Age and RestingECG": 0.03654,
    "Age and MaxHR": 0.01928,
    "Age and ExerciseAngina": 0.00138,
    "Age and Oldpeak": 0.99969,
    "Age and ST_Slope": 0.01690,
    "Age and HeartDisease": 0.00001,
    "Sex and ChestPainType": 0.00000,
    "Sex and RestingBP": 0.78306,
    "Sex and Cholesterol": 0.06093,
    "Sex and FastingBS": 0.00168,
    "Sex and RestingECG": 0.49360,
    "Sex and MaxHR": 0.83364,
    "Sex and ExerciseAngina": 0.00005,
    "Sex and Oldpeak": 0.71862,
    "Sex and ST_Slope": 0.00030,
    "Sex and HeartDisease": 0.00000,
    "ChestPainType and RestingBP": 0.85288,
    "ChestPainType and Cholesterol": 0.00178,
    "ChestPainType and FastingBS": 0.00000,
    "ChestPainType and RestingECG": 0.08041,
    "ChestPainType and MaxHR": 0.08228,
    "ChestPainType and ExerciseAngina": 0.00000,
    "ChestPainType and Oldpeak": 0.00014,
    "ChestPainType and ST_Slope": 0.00000,
    "ChestPainType and HeartDisease": 0.00000
}

# Sort the associations based on their p-values
sorted_associations = sorted(associations.items(), key=lambda x: x[1])

# Extract the association names and p-values into separate lists
associations_list = [x[0] for x in sorted_associations]
p_values_list = [x[1] for x in sorted_associations]

# Create a bar chart of the associations and their p-values
plt.figure(figsize=(12, 8))
plt.barh(associations_list, p_values_list, color='purple')
plt.xlabel('p-value')
plt.title('Associations and their p-values')
plt.tight_layout()

# Show the chart
plt.show()


print('Pie Chart >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# Define the data
male_heart_disease = 20
male_no_heart_disease = 80
female_heart_disease = 10
female_no_heart_disease = 90

# Define the labels and colors
labels = ['Male Heart Disease', 'Male No Heart Disease', 'Female Heart Disease', 'Female No Heart Disease']
colors = ['red', 'orange', 'pink', 'lightcoral']

# Define the sizes
sizes = [male_heart_disease, male_no_heart_disease, female_heart_disease, female_no_heart_disease]

# Create the pie chart
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Add a title
plt.title('Heart Disease Cases by Gender')

# Show the chart
plt.show()


