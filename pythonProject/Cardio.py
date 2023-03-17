import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
# import tensorflow as tf
# import keras
import torch
import os

print(os.getcwd(), "\n")

# load the dataset
data = pd.read_csv('heart.csv', delimiter=',')
print("Head:\n", data.head(), "\n") #display the first few rows of the DataFrame
print("Shape:\n", data.shape, "\n") #returns the dimensions (rows, columns) of the DataFrame as a tuple
print(data.info(), "\n") #provides information about the DataFrame
print("Describe:\n", data.describe(), "\n") #provides descriptive statistics about each column in the DataFrame

#Preprocess the data
