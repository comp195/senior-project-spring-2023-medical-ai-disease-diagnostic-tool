import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab as pl
from pyexpat import model

from scipy.stats import chi2_contingency
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from data_loader import data_loader
import seaborn as sns
from scipy import stats
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


# Preprocess the data
def data_preprocess(file, use_outliers=True):
    data_load = file[0]
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

    heart_disease_yes = data_load[data_load['HeartDisease'] == 1]
    heart_disease_no = data_load[data_load['HeartDisease'] == 0]

    plt.hist([heart_disease_yes['Age'], heart_disease_no['Age']], alpha=0.5)
    plt.xlabel('Age')
    plt.ylabel('Number of Patients')
    plt.legend(['1', '0'])
    plt.title('Relationship')
    plt.show()

    disease_by_sex = data_load.groupby(['Sex', 'HeartDisease']).size().unstack()  # Count the incidences by Sex and
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

    plt.hist([heart_disease_yes['RestingBP'], heart_disease_no['RestingBP']], alpha=0.5)
    plt.xlabel('Resting blood pressure (in mm Hg on admission to the hospital)')
    plt.ylabel('Number of Patients')
    plt.title('Relationship')
    plt.show()

    plt.hist([heart_disease_yes['Cholesterol'], heart_disease_no['Cholesterol']], alpha=0.5)
    plt.xlabel('Cholesterol in mg/dl')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship')
    plt.show()

    sns.countplot(x='FastingBS', hue='HeartDisease', data=data_load)
    plt.xlabel('Fasting blood sugar > 120 mg/dl')
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

    plt.hist([heart_disease_yes['MaxHR'], heart_disease_no['MaxHR']], alpha=0.5)
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

    plt.hist([heart_disease_yes['Oldpeak'], heart_disease_no['Oldpeak']], alpha=0.5)
    plt.xlabel('ST depression induced by exercise relative to rest')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Oldpeak-HeartDisease Connection')
    plt.show()

    disease_by_sts = data_load.groupby(['ST_Slope', 'HeartDisease']).size().unstack()
    disease_by_sts.plot(kind='bar', stacked=True)
    plt.xlabel('The slope of the peak exercise ST segment')
    plt.ylabel('Number of Patients with Heart Disease')
    plt.title('Relationship')
    plt.show()

    corr_matrix = data_load.corr()
    sns.heatmap(corr_matrix, annot=True, cmap="YlGnBu")
    plt.show()

    #       Identify outliers - visualization of distribution of variables and statistically

    # Detect outliers using visuals
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
    plt.title('Distribution of Fasting Blood Sugars')
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

    # calculate the mean, median, standard deviation, minimum, and maximum values of each column
    mean_age = data_load['Age'].mean()
    median_age = data_load['Age'].median()
    std_dev_age = data_load['Age'].std()
    min_age = data_load['Age'].min()
    max_age = data_load['Age'].max()

    print("Mean Age:", mean_age)
    print("Median Age:", median_age)
    print("Standard deviation of Age:", std_dev_age)
    print("Minimum Age:", min_age)
    print("Maximum Age:", max_age, "\n")

    mean_rbp = data_load['RestingBP'].mean()
    median_rbp = data_load['RestingBP'].median()
    std_dev_rbp = data_load['RestingBP'].std()
    min_rbp = data_load['RestingBP'].min()
    max_rbp = data_load['RestingBP'].max()

    print("Mean Resting Blood Pressures:", mean_rbp)
    print("Median Resting Blood Pressures:", median_rbp)
    print("Standard deviation of Resting Blood Pressures:", std_dev_rbp)
    print("Minimum Resting Blood Pressures:", min_rbp)
    print("Maximum Resting Blood Pressures:", max_rbp, "\n")

    mean_chol = data_load['Cholesterol'].mean()
    median_chol = data_load['Cholesterol'].median()
    std_dev_chol = data_load['Cholesterol'].std()
    min_chol = data_load['Cholesterol'].min()
    max_chol = data_load['Cholesterol'].max()

    print("Mean Cholesterol:", mean_chol)
    print("Median Cholesterol:", median_chol)
    print("Standard deviation of Cholesterol:", std_dev_chol)
    print("Minimum Cholesterol:", min_chol)
    print("Maximum Cholesterol:", max_chol, "\n")

    mean_mhr = data_load['MaxHR'].mean()
    median_mhr = data_load['MaxHR'].median()
    std_dev_mhr = data_load['MaxHR'].std()
    min_mhr = data_load['MaxHR'].min()
    max_mhr = data_load['MaxHR'].max()

    print("Mean Maximum Heart Rate:", mean_mhr)
    print("Median Maximum Heart Rate:", median_mhr)
    print("Standard deviation of Maximum Heart Rate:", std_dev_mhr)
    print("Minimum Maximum Heart Rate:", min_mhr)
    print("Maximum Maximum Heart Rate:", max_mhr, "\n")

    mean_op = data_load['Oldpeak'].mean()
    median_op = data_load['Oldpeak'].median()
    std_dev_op = data_load['Oldpeak'].std()
    min_op = data_load['Oldpeak'].min()
    max_op = data_load['Oldpeak'].max()

    print("Mean Exercise-induced ST depressions:", mean_op)
    print("Median Exercise-induced ST depressions:", median_op)
    print("Standard deviation of Exercise-induced ST depressions:", std_dev_op)
    print("Minimum Exercise-induced ST depressions:", min_op)
    print("Maximum Exercise-induced ST depressions:", max_op, "\n")

    #       Handle Outliers - Outliers may be removed or adjusted. Outliers may be removed if they are data input
    #                         mistakes or affect model performance. You may also replace outliers with more realistic
    #                         numbers. Capping, where extreme values are replaced with the maximum or lowest value
    #                         within a range, or winsorization, where extreme values are replaced with data at a
    #                         specified percentile, may achieve this.

    numerical_data = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
    categorical_data = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']

    def outliers_zscore(data):
        z_scores = stats.zscore(data)
        abs_zscores = np.abs(z_scores)  # calculates z-scores for each value and takes the absolute values
        threshold = 3
        return abs_zscores > threshold  # returns a Boolean array that says for each value whether it is an outlier.

    def numerical_zscore(df, use_outliers=True):
        for col in numerical_data:  # iterates through each numerical column
            col_data = df[col]
            if use_outliers:
                outliers = col_data[outliers_zscore(col_data)]  # applies the outliers_zscore function to each column
                if len(outliers) > 0:
                    print(f"Outliers in {col}:")
                    print(outliers, "\n")  # prints the outliers for each column if any
                    col_mean = col_data.mean()  # gets the mean of each column
                    col_std = col_data.std()  # gets the standard deviation of each column
                    col_min = col_mean - 3 * col_std  # Subtracting 3 times the standard deviation from the mean lowers
                    #                                   the column's "normal" or "acceptable" values. Outliers fall
                    #                                   below this.
                    col_max = col_mean + 3 * col_std  # Adding 3 times the standard deviation to the mean determines a
                    #                                   column's "normal" or "acceptable" upper limit. Outliers surpass
                    #                                   it too.
                    col_data = np.clip(col_data, col_min, col_max)  # capping method
                else:
                    print(f"No outliers in {col}\n")
            else:
                print(f'Without outliers in {col}\n')
                col_mean = col_data.mean()
                col_std = col_data.std()
                df = df[(df[col] >= col_mean - 3 * col_std) & (df[col] <= col_mean + 3 * col_std)]  # remove outliers
                print(col_data.describe(), '\n')
        return df

    def categorical_zscore(df):
        for col in categorical_data:  # iterates through each categorical column
            col_data = df[col]
            freq = col_data.value_counts(normalize=True)  # calculates the frequency of each category
            if len(freq) < 10:
                print(freq, "\n")  # prints the frequency distribution if the number of categories is less than 10
            else:
                print(f"Frequency distribution for {col} has too many categories to display.\n")

    numerical_zscore(data_load)
    categorical_zscore(data_load)

    # Data Encoding - If the dataset has categorical features, like gender or type of disease, you should turn them into
    #                 numbers that the model can use.

    col_encode = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
    data_load_encode = pd.get_dummies(data_load, columns=col_encode)

    # Data Scaling - Make sure that all the features are the same size by putting them on the same scale to make sure
    #                that high-value features don't take over the model and skew the results.

    scaler = MinMaxScaler()  # scale the numerical columns of the dataset to the same range.
    cols = data_load.select_dtypes(include='number').columns.tolist()  # Pick just numerical dataset columns by
    #                                                                    checking for numerical data types and saving
    #                                                                    their column names in a list.
    data_load[cols] = scaler.fit_transform(data_load[cols])  # identify the numerical and category columns

    # Data Features - Choose the dataset's most important features that can be used to make predictions. To find the
    #                 most important features, you can use methods like correlation analysis, the chi-squared test,
    #                 or recursive feature elimination.
    print('Chi-Squared Test >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    # Loop through all pairs of categorical features and calculate the chi-square statistic and p-value
    for i in col_encode:
        contingency_table = pd.crosstab(data_load[i], data_load['HeartDisease'])
        chi2, p, dof, expected = chi2_contingency(contingency_table)
        print(f'{i}: Chi-square test = {chi2}, p = {p}')

    print('Correlation Analysis >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

    corr_matrix = data_load_encode.corr()  # calculate the correlation matrix
    corr_with_target = corr_matrix['HeartDisease'].sort_values(ascending=False)
    print(corr_with_target)

    # Data Splitting - Separate the data into sets for training and sets for testing.

    x = data_load.drop('HeartDisease', axis=1)  # separate features and the target variable
    y = data_load['HeartDisease']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    return data_load


file = data_loader()
processed_data = data_preprocess(file)

'''

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

    # create a figure with subplots for each column
    fig, axs = plt.subplots(nrows=4, ncols=3, figsize=(15, 10))
    plt.subplots_adjust(hspace=0.5)

    # loop over each column and plot a histogram
    for i, col in enumerate(data_load.columns[:-1]):
        sns.histplot(data_load[col], kde=False, ax=axs[i // 3, i % 3])
        axs[i // 3, i % 3].set_title(f'Distribution of {col}')
        axs[i // 3, i % 3].set_xlabel(col)
        axs[i // 3, i % 3].set_ylabel('Number of Patients')

    plt.show()
    
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
    fig, axes = plt.subplots(nrows=len(cols), ncols=len(cols), figsize=(10, 10))

    # Loop through all variables and create scatter plot with best fit line
    for i, var1 in enumerate(cols):
        for j, var2 in enumerate(cols):
            if i == j:
                # Create empty plot if variables are the same
                axes[i, j].axis('off')
            else:
                # Create scatter plot with color based on correlation
                color = 'r' if df[var1].corr(df[var2]) > 0 else 'b'
                sns.regplot(ax=axes[i, j], x=var1, y=var2, data=df, color=color)
                # Add best fit line to scatter plot
                sns.regplot(ax=axes[i, j], x=var1, y=var2, data=df, line_kws={'color': 'k'}, scatter=False)
                # Add title to scatter plot
                axes[i, j].set_title(f"{var1} vs {var2}")
                # Set x and y axis labels for scatter plot
                axes[i, j].set_xlabel(var1)
                axes[i, j].set_ylabel(var2)

    plt.suptitle("Scatter Plots with Best Fit Line for Correlation Matrix", fontsize=16)
    plt.tight_layout()
    plt.show()

    print('Recursive Feature Elimination >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

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

    print('Pie Chart>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
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

'''
