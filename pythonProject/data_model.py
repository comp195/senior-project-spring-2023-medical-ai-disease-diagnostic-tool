# Libraries we need for this project

import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB

# Load the preprocessed data and selected features from the CSV files
processed_data = pd.read_csv('processed_data.csv')
corr_features = pd.read_csv('corr_features.csv', header=None).iloc[:, 0].tolist()
chi2_features = pd.read_csv('chi2_features.csv', header=None).iloc[:, 0].tolist()
rfe_features = pd.read_csv('rfe_features.csv', header=None).iloc[:, 0].tolist()

# Create a dictionary containing the names and lists of different feature sets
feature_sets = {
    'all_features': processed_data.drop('HeartDisease', axis=1).columns.tolist(),  # All features in the dataset
    'corr_features': corr_features,  # Top 10 features based on correlation
    'chi_features': chi2_features,  # Top 10 features based on Chi-squared test
    'rfe_features': rfe_features,  # Top 10 features based on Recursive Feature Elimination
}
print(feature_sets)

highest_scores = {
    'Logistic Regression': 0,
    'Random Forest': 0,
    'Naive Bayes': 0,
}

# Iterate through the feature sets
for name, features in feature_sets.items():
    X = processed_data[features]  # Choose the features that belong to the current set of features.
    y = processed_data['HeartDisease']  # Set the term 'HeartDisease' as the goal.

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    lr_model = LogisticRegression()  # Put the logistic regression model into action
    lr_model.fit(X_train, y_train)  # Use the training data to fit the model.

    lr_y_pred = lr_model.predict(X_test)  # Make predictions based on the test results
    lr_accuracy = accuracy_score(y_test, lr_y_pred)  # Figure out how accurate the model's predictions are.

    if lr_accuracy > highest_scores['Logistic Regression']:
        highest_scores['Logistic Regression'] = lr_accuracy

    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)

    rf_y_pred = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_y_pred)

    if rf_accuracy > highest_scores['Random Forest']:
        highest_scores['Random Forest'] = rf_accuracy

    nb_model = GaussianNB()
    nb_model.fit(X_train,y_train)

    nb_y_pred = nb_model.predict(X_test)
    nb_accuracy = accuracy_score(y_test, nb_y_pred)

    if nb_accuracy > highest_scores['Naive Bayes']:
        highest_scores['Naive Bayes'] = nb_accuracy

    print(f"Accuracy for {name}(Logistic Regression): {lr_accuracy}")  # Print the accuracy for the current feature set
    print(f"Accuracy for {name} (Random Forest): {rf_accuracy}")
    print(f"Accuracy for {name} (Naive Bayes): {nb_accuracy}")

    highest_scores[f"{name}(Logistic Regression)"] = lr_accuracy
    highest_scores[f"{name}(Random Forest)"] = rf_accuracy
    highest_scores[f"{name}(Naive Bayes)"] = nb_accuracy

highest_accuracy = max(highest_scores, key=highest_scores.get)

plt.figure(figsize=(10, 8))
sns.barplot(x=list(highest_scores.values()), y=list(highest_scores.keys()))
plt.title(f"Highest accuracy: {highest_accuracy}: {highest_scores[highest_accuracy]}")
plt.xlabel("Accuracy")
plt.ylabel("Model and Feature Set")
plt.show()
plt.tight_layout()