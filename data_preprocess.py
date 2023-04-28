from sklearn.preprocessing import MinMaxScaler
from data_loader import data_loader
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
import seaborn as sns
import matplotlib.pyplot as plt

# Preprocess the data
def data_preprocess(input_data, use_outliers=True, mode='training'):
    """
    Encoding category variables, scaling numerical variables, and controlling outliers are all used to preprocess the incoming dataset.

    Args: df (pandas.DataFrame): The dataset to be preprocessed.
        use_outliers (bool, optional): Whether or not to handle data outliers. True is the default value.
        mode (str, optional): The operation mode, either 'training' or 'prediction'. 'Training' is the default setting.

    Pandas are the results.The preprocessed dataset is represented by DataFrame.


    """

    data = input_data.copy()

    # Data Cleaning - remove mistakes, inconsistencies, and missing values using imputation, outlier identification,
    #                 and data deduplication.
    if mode == 'training':
        if data.isnull().sum().sum() > 0:  # checks for null or missing values and counts the missing values, and
            #                                     compares the result to 0.
            print(f"Warning: {data.isnull().sum().sum()} missing values.")
            data.fillna(data.mean(), inplace=True)  # Use the average of the feature to fill in the missing values
        else:
            print("No missing values.")

        if data.duplicated().sum() > 0:  # count the total number of duplicated rows in the entire dataset.
            print(f"Warning: {data.duplicated().sum()} duplicates")
            data.drop_duplicates(inplace=True)  # remove duplicates
        else:
            print("No duplicate values")

        #       Visualization of correlation between variables and target variable
        if 'HeartDisease' in data.columns:
            heart_disease_yes = data[data['HeartDisease'] == 1]
            heart_disease_no = data[data['HeartDisease'] == 0]

            plt.hist([heart_disease_yes['Age'], heart_disease_no['Age']], alpha=0.5)
            plt.xlabel('Age')
            plt.ylabel('Number of Patients')
            plt.legend(['1', '0'])
            plt.title('Relationship')
            plt.show()

            disease_by_sex = data.groupby(['Sex', 'HeartDisease']).size().unstack()  # Count the incidences by Sex and
            #                                                                          HeartDisease.
            disease_by_sex.plot(kind='bar', stacked=True)  # create a stacked bar chart
            plt.xlabel('Heart Disease')
            plt.ylabel('Number of Patients')
            plt.title('Relationship')
            plt.show()

            disease_by_cpt = data.groupby('ChestPainType')['HeartDisease'].sum()
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

            sns.countplot(x='FastingBS', hue='HeartDisease', data=data)
            plt.xlabel('Fasting blood sugar > 120 mg/dl')
            plt.ylabel('Number of Patients')
            plt.title('Heart Disease Patients by Fasting Blood Sugar Level')
            plt.show()

            resting_ecg_counts = data['RestingECG'].value_counts()
            disease_by_resting_ecg = data.groupby('RestingECG')['HeartDisease'].sum()
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

            disease_by_ea = data.groupby(['ExerciseAngina', 'HeartDisease'])['HeartDisease'].count()
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

            disease_by_sts = data.groupby(['ST_Slope', 'HeartDisease']).size().unstack()
            disease_by_sts.plot(kind='bar', stacked=True)
            plt.xlabel('The slope of the peak exercise ST segment')
            plt.ylabel('Number of Patients with Heart Disease')
            plt.title('Relationship')
            plt.show()

        #       Identify outliers - visualization of distribution of variables and statistically

        # Detect outliers using visuals
        age_data = data['Age']
        sns.histplot(age_data, kde=False)  # create histogram
        plt.title('Distribution of Ages')
        plt.xlabel('Age')
        plt.ylabel('Number of Patents')
        plt.show()

        sex_data = data['Sex']
        sns.histplot(sex_data, kde=False)
        plt.title('Distribution of Sex')
        plt.xlabel('Sex')
        plt.ylabel('Number of Patients')
        plt.show()

        cpt_data = data['ChestPainType']
        sns.histplot(cpt_data, kde=False)
        plt.title('Distribution of Chest Pain Types')
        plt.xlabel('Chest Pain Type')
        plt.ylabel('Number of Patients')
        plt.show()

        rbp_data = data['RestingBP']
        sns.histplot(rbp_data, kde=False)
        plt.title('Distribution of Resting Blood Pressures')
        plt.xlabel('Resting Blood Pressure')
        plt.ylabel('Number of Patients')
        plt.show()

        chol_data = data['Cholesterol']
        sns.histplot(chol_data, kde=False)
        plt.title('Distribution of Cholesterol')
        plt.xlabel('Cholesterol')
        plt.ylabel('Number of Patients')
        plt.show()

        fbs_data = data['FastingBS']
        sns.histplot(fbs_data, kde=False)
        plt.title('Distribution of Fasting Blood Sugars')
        plt.xlabel('Fasting Blood Pressure')
        plt.ylabel('Number of Patients')
        plt.show()

        recg_data = data['RestingECG']
        sns.histplot(recg_data, kde=False)
        plt.title('Distribution of Resting Electrocardiograms')
        plt.xlabel('Resting Electrocardiograms')
        plt.ylabel('Number of Patients')
        plt.show()

        mhr_data = data['MaxHR']
        sns.histplot(mhr_data, kde=False)
        plt.title('Distribution of Maximum Heart Rates')
        plt.xlabel('Maximum Heart Rates')
        plt.ylabel('Number of Patients')
        plt.show()

        ea_data = data['ExerciseAngina']
        sns.histplot(ea_data, kde=False)
        plt.title('Distribution of Exercise-induced angina')
        plt.xlabel('Exercise-induced angina')
        plt.ylabel('Number of Patients')
        plt.show()

        op_data = data['Oldpeak']
        sns.histplot(op_data, kde=False)
        plt.title('Distribution of Exercise-induced ST depressions')
        plt.xlabel('Exercise-induced ST depressions')
        plt.ylabel('Number of Patients')
        plt.show()

        sts_data = data['ST_Slope']
        sns.histplot(sts_data, kde=False)
        plt.title('Distribution of ST segment slope')
        plt.xlabel('ST segment slope')
        plt.ylabel('Number of Patients')
        plt.show()

        # calculate the mean, median, standard deviation, minimum, and maximum values of each column
        mean_age = data['Age'].mean()
        median_age = data['Age'].median()
        std_dev_age = data['Age'].std()
        min_age = data['Age'].min()
        max_age = data['Age'].max()

        print("Mean Age:", mean_age)
        print("Median Age:", median_age)
        print("Standard deviation of Age:", std_dev_age)
        print("Minimum Age:", min_age)
        print("Maximum Age:", max_age, "\n")

        mean_rbp = data['RestingBP'].mean()
        median_rbp = data['RestingBP'].median()
        std_dev_rbp = data['RestingBP'].std()
        min_rbp = data['RestingBP'].min()
        max_rbp = data['RestingBP'].max()

        print("Mean Resting Blood Pressures:", mean_rbp)
        print("Median Resting Blood Pressures:", median_rbp)
        print("Standard deviation of Resting Blood Pressures:", std_dev_rbp)
        print("Minimum Resting Blood Pressures:", min_rbp)
        print("Maximum Resting Blood Pressures:", max_rbp, "\n")

        mean_chol = data['Cholesterol'].mean()
        median_chol = data['Cholesterol'].median()
        std_dev_chol = data['Cholesterol'].std()
        min_chol = data['Cholesterol'].min()
        max_chol = data['Cholesterol'].max()

        print("Mean Cholesterol:", mean_chol)
        print("Median Cholesterol:", median_chol)
        print("Standard deviation of Cholesterol:", std_dev_chol)
        print("Minimum Cholesterol:", min_chol)
        print("Maximum Cholesterol:", max_chol, "\n")

        mean_mhr = data['MaxHR'].mean()
        median_mhr = data['MaxHR'].median()
        std_dev_mhr = data['MaxHR'].std()
        min_mhr = data['MaxHR'].min()
        max_mhr = data['MaxHR'].max()

        print("Mean Maximum Heart Rate:", mean_mhr)
        print("Median Maximum Heart Rate:", median_mhr)
        print("Standard deviation of Maximum Heart Rate:", std_dev_mhr)
        print("Minimum Maximum Heart Rate:", min_mhr)
        print("Maximum Maximum Heart Rate:", max_mhr, "\n")

        mean_op = data['Oldpeak'].mean()
        median_op = data['Oldpeak'].median()
        std_dev_op = data['Oldpeak'].std()
        min_op = data['Oldpeak'].min()
        max_op = data['Oldpeak'].max()

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
                        df[col] = np.clip(col_data, col_min, col_max)  # capping method
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
            for col in categorical_data:
                col_data = df[col]
                freq = col_data.value_counts(normalize=True)
                if len(freq) < 10:
                    print(freq, "\n")
                else:
                    print(f"Top 10 categories for {col}:")
                    print(freq.head(10), "\n")

        numerical_zscore(data)
        categorical_zscore(data)

        # Visualize the distribution of numerical variables
        def visualize_numerical(df, cols):
            for col in cols:
                plt.figure(figsize=(8, 4))
                sns.histplot(df[col], kde=True)
                plt.title(f"Distribution of {col}")
                plt.show()

        # Perform feature scaling or normalization
        def scale_features(df, cols, input_scaler=None):
            if input_scaler is None:
                input_scaler = MinMaxScaler()
                scaled_data = input_scaler.fit_transform(df[cols])
            else:
                scaled_data = input_scaler.transform(df[cols])

            scaled_df = pd.DataFrame(scaled_data, columns=cols, index=df.index)
            df.drop(cols, axis=1, inplace=True)
            df = pd.concat([df, scaled_df], axis=1)

            return df, input_scaler

        def encode_categorical(df, cols):
            df = pd.get_dummies(df, columns=cols, drop_first=True)
            return df

        numerical_zscore(data)
        visualize_numerical(data, numerical_data)
        categorical_zscore(data)
        data, fitted_scaler = scale_features(data, numerical_data)
        data = encode_categorical(data, categorical_data)

        #print(data)

        # Data Features - Choose the dataset's most important features that can be used to make predictions. To find the
        #                 most important features, you can use methods like correlation analysis, the chi-squared test,
        #                 or recursive feature elimination.
        print('Chi-Squared Test >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        # Loop through all pairs of categorical features and calculate the chi-square statistic and p-value
        X = data.drop("HeartDisease", axis=1)
        y = data["HeartDisease"]
        chi2_selector = SelectKBest(chi2, k=10)
        chi2_selector.fit(X, y)
        chi2_features = X.columns[chi2_selector.get_support()].tolist()
        print("Top 10 features using Chi-Squared Test:", chi2_features)

        print('Correlation Analysis >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

        corr_matrix = data.corr()  # calculate the correlation matrix
        print("Correlation Matrix:")
        print(corr_matrix)
        plt.figure(figsize=(15, 10))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
        plt.title("Feature Correlations")
        plt.tight_layout()
        plt.show()

        # Get the absolute correlation coefficients and sort the features based on their correlation with HeartDisease
        abs_corr_coeffs = corr_matrix['HeartDisease'].apply(lambda x: abs(x)).sort_values(ascending=False)
        print("\nAbsolute correlation coefficients with HeartDisease:")
        print(abs_corr_coeffs)
        # Get the top 10 features based on their correlation with HeartDisease
        corr_features = abs_corr_coeffs.iloc[1:11].index.tolist()
        print("\nTop 10 features using correlation analysis:")
        print(corr_features)

        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        model = LogisticRegression(solver='liblinear')
        rfe = RFE(model, n_features_to_select=10)
        rfe = rfe.fit(X, y)
        rfe_features = X.columns[rfe.get_support()].tolist()
        print("Top 10 features using Recursive Feature Elimination:", rfe_features)

        expected_columns = ['FastingBS', 'Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak',
                            'Sex_M', 'Sex_F',
                            'ChestPainType_ATA', 'ChestPainType_NAP', 'ChestPainType_TA', 'ChestPainType_ASY',
                            'RestingECG_Normal', 'RestingECG_ST', 'RestingECG_LVH',
                            'ExerciseAngina_Y', 'ExerciseAngina_N',
                            'ST_Slope_Flat', 'ST_Slope_Up', 'ST_Slope_Down']

        for col in expected_columns:
            if col not in data.columns:
                data[col] = 0

        # Reorder the columns in the DataFrame to match the expected order
        data = data[expected_columns]

        return data, corr_features, chi2_features, rfe_features, fitted_scaler

    elif mode == 'prediction':
        data_new = {
            'Age': data.loc[0, 'Age'],
            'RestingBP': data.loc[0, 'RestingBP'],
            'Cholesterol': data.loc[0, 'Cholesterol'],
            'FastingBS': data.loc[0, 'FastingBS'],
            'MaxHR': data.loc[0, 'MaxHR'],
            'Oldpeak': data.loc[0, 'Oldpeak'],
            'Sex_F': 1 if data.loc[0, 'Sex'] == 'female' else 0,
            'Sex_M': 1 if data.loc[0, 'Sex'] == 'male' else 0,
            'ChestPainType_ASY': 1 if data.loc[0, 'ChestPainType'] == 'asymptomatic' else 0,
            'ChestPainType_ATA': 1 if data.loc[0, 'ChestPainType'] == 'atypical-angina' else 0,
            'ChestPainType_NAP': 1 if data.loc[0, 'ChestPainType'] == 'non-anginal-pain' else 0,
            'ChestPainType_TA': 1 if data.loc[0, 'ChestPainType'] == 'typical-angina' else 0,
            'RestingECG_LVH': 1 if data.loc[0, 'RestingECG'] == 'left-ventricular-hypertrophy' else 0,
            'RestingECG_Normal': 1 if data.loc[0, 'RestingECG'] == 'normal' else 0,
            'RestingECG_ST': 1 if data.loc[0, 'RestingECG'] == 'st-t-wave-abnormality' else 0,
            'ExerciseAngina_N': 1 if data.loc[0, 'ExerciseAngina'] == 0 else 0,
            'ExerciseAngina_Y': 1 if data.loc[0, 'ExerciseAngina'] == 1 else 0,
            'ST_Slope_Down': 1 if data.loc[0, 'ST_Slope'] == 'down-sloping' else 0,
            'ST_Slope_Flat': 1 if data.loc[0, 'ST_Slope'] == 'flat' else 0,
            'ST_Slope_Up': 1 if data.loc[0, 'ST_Slope'] == 'up-sloping' else 0,
        }

        input_data = pd.DataFrame([data_new])

        numerical_features = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
        fitted_scaler = MinMaxScaler(feature_range=(0, 1))
        input_data[numerical_features] = fitted_scaler.fit_transform(input_data[numerical_features])

        return input_data, fitted_scaler

    else:
        raise ValueError("Invalid mode specified. Use either 'training' or 'prediction'.")


if __name__ == "__main__":
    raw_data = data_loader()[0]
    processed_data, corr_features, chi2_features, rfe_features, scaler = data_preprocess(raw_data, mode='training')

    preprocessed_data_with_target = pd.concat([processed_data, raw_data['HeartDisease']], axis=1)
    preprocessed_data_with_target.to_csv('processed_data.csv', index=False)
    pd.DataFrame(corr_features).to_csv('corr_features.csv', header=False, index=False)
    pd.DataFrame({'chi2_features': chi2_features}).to_csv('chi2_features.csv', header=False, index=False)
    pd.DataFrame({'rfe_features': rfe_features}).to_csv('rfe_features.csv', header=False, index=False)

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
    
        # Data Splitting - Separate the data into sets for training and sets for testing.

    x = data_load.drop('HeartDisease', axis=1)  # separate features and the target variable
    y = data_load['HeartDisease']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)

    train_data = pd.concat([x_train, y_train], axis=1)
    train_data.to_csv('training_data.csv', index=False)

    return x_train, y_train

'''
