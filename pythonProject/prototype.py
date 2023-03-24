# Libraries we need for this project

import inline as inline
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas.core.frame
import seaborn as sns

import os

from numpy import array

print(os.listdir())

import warnings

warnings.filterwarnings('ignore')

# our dataset from kaggle

dataset = pd.read_csv("heart.csv")

if 'target' not in dataset.colums:
    print("Error: 'target column not found in DataFrame")
else:
    print(dataset['target'].describe())

# our dataframe  and object in pandas

type(dataset)
pandas.core.frame.DataFrame

# dataset Shape
dataset.shape
(900, 10)

# Print some columns
dataset.head(15)

dataset.sample(5)

dataset.describe()

dataset.info()
info = ["age", "1: male, 0: female",
        "chest pain type, 1: typical angina, 2: atypical angina, 3: non-anginal pain, 4: asymptomatic",
        "resting blood pressure", " serum cholesterol in mg/dl", "fasting blood sugar > 120 mg/dl",
        "resting electrocardiograph results (values 0,1,2)", " maximum heart rate achieved",
        "exercise induced angina", "oldpeak = ST depression induced by exercise relative to rest",
        "the slope of the peak exercise ST segment", "number of major vessels (0-3) colored by fluoroscopy",
        "thal: 3 = normal; 6 = fixed defect; 7 = reversible defect"]

for i in range(len(info)):
    print(dataset.columns[i] + ":\t\t\t" + info[i])

    dataset["target"].describe()
    print(dataset["target"].describe())
    print(dataset.columns)

    dataset["target"].unique()
    array([1, 0])

    print(dataset.corr()["target"].abs().sort_values(ascending=False))

    y = dataset["target"]
    sns.countplot(y)

    target_temp = dataset.target.value_counts()
    print(target_temp)

    print("Percentage of patience without heart problems: " + str(round(target_temp[0] * 100 / 303, 2)))
    print("Percentage of patience with heart problems: " + str(round(target_temp[1] * 100 / 303, 2)))


    dataset["sex"].unique()
    array([1, 0])

    sns.barplot(dataset["sex"], y)

    dataset["cp"].unique()
    sns.barplot(dataset["cp"], y)
    dataset["fbs"].describe()
    dataset["fbs"].unique()
    sns.barplot(dataset["fbs"], y)
    dataset["restecg"].unique()
    sns.barplot(dataset["restecg"], y)
    dataset["exang"].unique()
    sns.barplot(dataset["exang"], y)
