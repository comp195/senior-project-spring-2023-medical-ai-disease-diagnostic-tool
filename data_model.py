# Libraries we need for this project
import pickle
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, roc_curve
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
# print(feature_sets)

highest_scores = {
    'Logistic Regression': 0,
    'Random Forest': 0,
    'Naive Bayes': 0,
}

highest_precision = {
    'Logistic Regression': 0,
    'Random Forest': 0,
    'Naive Bayes': 0,
}
highest_recall = {
    'Logistic Regression': 0,
    'Random Forest': 0,
    'Naive Bayes': 0,
}

LR_MODEL_ALL_FEATURES = 0
RF_ALL_FEATURES = 0
NB_ALL_FEATURES = 0

# Iterate through the feature sets
for name, features in feature_sets.items():
    X = processed_data[features]  # Choose the features that belong to the current set of features.
    y = processed_data['HeartDisease']  # Set the term 'HeartDisease' as the goal.

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    lr_model = LogisticRegression()

    # Put the logistic regression model into action
    lr_model.fit(X_train, y_train)  # Use the training data to fit the model.
    lr_y_pred = lr_model.predict(X_test)  # Make predictions based on the test results
    lr_accuracy = accuracy_score(y_test, lr_y_pred)  # Figure out how accurate the model's predictions are.
    lr_precision = precision_score(y_test, lr_y_pred)
    lr_recall = recall_score(y_test, lr_y_pred)
    lr_fpr, lr_tpr, lr_thresholds = roc_curve(y_test, lr_y_pred)
    lr_auc = roc_auc_score(y_test, lr_y_pred)

    plt.plot(lr_fpr, lr_tpr, label=f"{name} (Logistic Regression), AUC={lr_auc}")

    if lr_accuracy > highest_scores['Logistic Regression']:
        highest_scores['Logistic Regression'] = lr_accuracy

    if lr_precision > highest_precision['Logistic Regression']:
        highest_precision['Logistic Regression'] = lr_precision

    if lr_recall > highest_recall['Logistic Regression']:
        highest_recall['Logistic Regression'] = lr_recall

    rf_model = RandomForestClassifier()  # Create a random forest classifier model instance
    rf_model.fit(X_train, y_train)  # Train the random forest model on the training data
    rf_y_pred = rf_model.predict(X_test)  # Use the random forest model to make predictions on the test data
    rf_accuracy = accuracy_score(y_test, rf_y_pred)  # Calculate the accuracy of the random forest's predictions
    rf_precision = precision_score(y_test, rf_y_pred)
    rf_recall = recall_score(y_test, rf_y_pred)
    rf_fpr, rf_tpr, rf_thresholds = roc_curve(y_test, rf_y_pred)
    rf_auc = roc_auc_score(y_test, rf_y_pred)

    plt.plot(rf_fpr, rf_tpr, label=f"{name} (Random Forest), AUC={rf_auc}")

    if rf_accuracy > highest_scores['Random Forest']:
        highest_scores['Random Forest'] = rf_accuracy

    if rf_precision > highest_precision['Random Forest']:
        highest_precision['Random Forest'] = rf_precision

    if rf_recall > highest_recall['Random Forest']:
        highest_recall['Random Forest'] = rf_recall

    nb_model = GaussianNB()  # Create a naive bayes model instance
    nb_model.fit(X_train, y_train)  # Train the naive bayes model on the training data

    nb_y_pred = nb_model.predict(X_test)  # Use the naive bayes model to make predictions on the test data
    nb_accuracy = accuracy_score(y_test, nb_y_pred)  # Calculate the accuracy of the naive bayes model's predictions
    nb_precision = precision_score(y_test, nb_y_pred)  # Calculate precision score
    nb_recall = recall_score(y_test, nb_y_pred)
    nb_fpr, nb_tpr, nb_thresholds = roc_curve(y_test, nb_y_pred)
    nb_auc = roc_auc_score(y_test, nb_y_pred)

    plt.plot(nb_fpr, nb_tpr, label=f"{name} (Naive Bayes), AUC={nb_auc}")

    if nb_accuracy > highest_scores['Naive Bayes']:
        highest_scores['Naive Bayes'] = nb_accuracy

    if nb_precision > highest_precision['Naive Bayes']:
        highest_precision['Naive Bayes'] = nb_precision

    if nb_recall > highest_recall['Naive Bayes']:
        highest_recall['Naive Bayes'] = nb_recall

    # Print the accuracy, precision and recall scores
    # print(f"Accuracy for {name}(Logistic Regression): {lr_accuracy}, Precision: {lr_precision}, Recall: {lr_recall}")
    # print(f"Accuracy for {name} (Random Forest): {rf_accuracy},  Precision: {rf_precision}, Recall: {rf_recall}")
    # print(f"Accuracy for {name} (Naive Bayes): {nb_accuracy}, Precision: {nb_precision}, Recall: {nb_recall}")

    # Add the highest accuracy, precision score for the current feature set and model to the dictionary
    highest_scores[f"{name}(Logistic Regression)"] = lr_accuracy
    highest_scores[f"{name}(Random Forest)"] = rf_accuracy
    highest_scores[f"{name}(Naive Bayes)"] = nb_accuracy
    highest_precision[f"{name}(Logistic Regression)"] = lr_precision
    highest_precision[f"{name}(Random Forest)"] = rf_precision
    highest_precision[f"{name}(Naive Bayes"] = nb_precision
    highest_recall[f"{name}(Logistic Regression"] = lr_recall
    highest_recall[f"{name}(Random Forest)"] = rf_recall
    highest_recall[f"{name}(Naive Bayes"] = nb_recall

    if name == "all_features":
        LR_MODEL_ALL_FEATURES = lr_model
        RF_ALL_FEATURES = rf_model
        NB_ALL_FEATURES = nb_model

if __name__ == "__main__":
    highest_accuracy = max(highest_scores, key=highest_scores.get)  # Find the model and feature set with the highest
    #                                                                 accuracy score
    highest_precision_model = max(highest_precision, key=highest_precision.get)
    highest_recall_model = max(highest_recall, key=highest_recall.get)

    # Create a bar plot with the accuracy scores and model/feature set names
    plt.figure(figsize=(10, 8))
    sns.barplot(x=list(highest_scores.values()), y=list(highest_scores.keys()))
    plt.title(f"Highest accuracy: {highest_accuracy}: {highest_scores[highest_accuracy]}")
    plt.xlabel("Accuracy")
    plt.ylabel("Model and Feature Set")
    plt.tight_layout()  # Add tight layout to the plot to prevent overlapping of labels and titles

    plt.figure(figsize=(10, 8))
    sns.barplot(x=list(highest_precision.values()), y=list(highest_precision.keys()))
    plt.title(f"Highest precision: {highest_precision_model}: {highest_precision[highest_precision_model]}")
    plt.xlabel("Precision")
    plt.ylabel("Model and Feature Set")
    plt.tight_layout()

    plt.figure(figsize=(10, 8))
    sns.barplot(x=list(highest_recall.values()), y=list(highest_recall.keys()))
    plt.title(f"Highest Recall: {highest_recall_model}: {highest_recall[highest_recall_model]}")
    plt.xlabel("Recall")
    plt.ylabel("Model and Feature Set")
    plt.tight_layout()
    plt.show()

    models = {
        'Logistic Regression': LR_MODEL_ALL_FEATURES,
        'Random Forest': RF_ALL_FEATURES,
        'Naive Bayes': NB_ALL_FEATURES,
    }

    for name, model in models.items():
        with open(f"{name}.pkl", "wb") as f:
            pickle.dump(model, f)
