# Libraries we need for this project

import inline as inline
import matplotlib
import pandas as pd
import pandas.core.frame
import seaborn as sns
import numpy as np
from scipy.stats import zscore
import os
from numpy import array
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras

from pythonProject.data_loader import data_loader

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




