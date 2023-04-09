import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import chi2_contingency
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight
from seaborn import heatmap
import seaborn as sns



from pythonProject.data_loader import data_loader


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

print('Newcorrelationgraph')

# read the data and calculate the correlation matrix
df = pd.read_csv('heart.csv')
corr_matrix = df.corr()

# create a figure with subplots
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

# plot Age vs. HeartDisease
sns.regplot(ax=axs[0, 0], data=df, x='Age', y='HeartDisease')

# plot RestingBP vs. HeartDisease
sns.regplot(ax=axs[0, 1], data=df, x='RestingBP', y='HeartDisease')

# plot Cholesterol vs. HeartDisease
sns.regplot(ax=axs[0, 2], data=df, x='Cholesterol', y='HeartDisease')

# plot FastingBS vs. HeartDisease
sns.regplot(ax=axs[1, 0], data=df, x='FastingBS', y='HeartDisease')

# plot MaxHR vs. HeartDisease
sns.regplot(ax=axs[1, 1], data=df, x='MaxHR', y='HeartDisease')

# plot Oldpeak vs. HeartDisease
sns.regplot(ax=axs[1, 2], data=df, x='Oldpeak', y='HeartDisease')

# set the title for the page
plt.suptitle('Correlation between Heart Disease and Selected Features')

# show the plots
plt.show()


print('scatterplots')



# Create sample dataframe
data = {'Age': [1.000000, 0.254078, -0.236358, 0.211500, -0.404093, 0.266694, 0.319918],
        'RestingBP': [0.254078, 1.000000, 0.102408, 0.021684, -0.126433, 0.142644, 0.052769],
        'Cholesterol': [-0.236358, 0.102408, 1.000000, 0.143055, -0.009940, 0.012608, -0.317407],
        'FastingBS': [0.211500, 0.021684, 0.143055, 1.000000, 0.046886, 0.100919, 0.353210],
        'MaxHR': [-0.404093, -0.126433, -0.009940, 0.046886, 1.000000, -0.122922, -0.372111],
        'Oldpeak': [0.266694, 0.142644, 0.012608, 0.100919, -0.122922, 1.000000, 0.421706],
        'HeartDisease': [0.319918, 0.052769, -0.317407, 0.353210, -0.372111, 0.421706, 1.000000]}

df = pd.DataFrame(data)

# Get column names of dataframe
cols = df.columns

# Create figure with subplots
fig, axes = plt.subplots(nrows=len(cols), ncols=len(cols), figsize=(10,10))

# Loop through all variables and create scatter plot with best fit line
for i, var1 in enumerate(cols):
    for j, var2 in enumerate(cols):
        if i == j:
            # Create empty plot if variables are the same
            axes[i,j].axis('off')
        else:
            # Create scatter plot with color based on correlation
            color = 'r' if df[var1].corr(df[var2]) > 0 else 'b'
            sns.regplot(ax=axes[i,j], x=var1, y=var2, data=df, color=color)
            # Add best fit line to scatter plot
            sns.regplot(ax=axes[i,j], x=var1, y=var2, data=df, line_kws={'color': 'k'}, scatter=False)
            # Add title to scatter plot
            axes[i,j].set_title(f"{var1} vs {var2}")
            # Set x and y axis labels for scatter plot
            axes[i,j].set_xlabel(var1)
            axes[i,j].set_ylabel(var2)

plt.suptitle("Scatter Plots with Best Fit Line for Correlation Matrix", fontsize=16)
plt.tight_layout()
plt.show()











