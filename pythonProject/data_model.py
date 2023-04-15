# Libraries we need for this project

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

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

    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)

    rf_y_pred = rf_model.predict(X_test)
    rf_accuracy = accuracy_score(y_test, rf_y_pred)

    print(f"Accuracy for {name}(Logistic Regression): {lr_accuracy}")  # Print the accuracy for the current feature set
    print(f"Accuracy for {name} (Random Forest): {rf_accuracy}")

'''
class Data_Model:
    model=None
    data =None
    def __init__(self):
        print('init called')
        data = pd.read_csv("heart.csv")
        data = self.clean_data(data)
        data.fillna(data.median(), inplace=True)
        self.data = data
        data_norm=data.apply(zscore)
        x= data_norm.drop('HeartDisease',axis =1)
        y= data['HeartDisease']
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2, random_state=42)
        model = keras.Sequential([
            keras.layers.Dense(16, activation='relu', input_shape = (11,)),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
        history = model.fit(x_train, y_train, epochs=10, batch_size=32, validation_data=(x_test, y_test))
        score = model.evaluate(x_test, y_test, verbose=0)
        print('Test loss:', score[0])
        print('Test accuracy:', score[1])
        self.model = model
        if self.model is None:
            print('111111111111')

    def predict_with_model(self, data):
        # function takes in data and returns the predictions for this data.
        # if there is missing value in the data it will autofill it.
        if self.model is None:
            print('model is None')
            return None
        data.fillna(self.data.median(), inplace=True)
        return self.model.predict(data)
    def clean_data (self, data):
        sex_mapping = {'M': 0, 'F': 1}
        ST_Slope_mapping = {'Flat': 0, 'Up': 1, 'Down': -1}
        ChestPainType_mapping = {'ASY': 0, 'NAP': 20, 'ATA': 50, 'TA': 70}
        ExerciseAngina_mapping = {'N': 0, 'Y': 1}
        RestingECG_mapping = {'Normal': 0, 'ST': 1}
        data['RestingECG'] = data['RestingECG'].map(RestingECG_mapping)
        data['ExerciseAngina'] = data['ExerciseAngina'].map(ExerciseAngina_mapping)
        data['ChestPainType'] = data['ChestPainType'].map(ChestPainType_mapping)
        data['ST_Slope'] = data['ST_Slope'].map(ST_Slope_mapping)
        data['Sex'] = data['Sex'].map(sex_mapping)
        return data
'''
