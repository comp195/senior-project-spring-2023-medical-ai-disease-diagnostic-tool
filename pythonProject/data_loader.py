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
def data_loader():
    data = pd.read_csv('heart.csv', delimiter=',')
    info_str = ""
    info_str += "Head:\n" + str(data.head(5)) + "\n"  # display the first few rows of the DataFrame
    info_str += "Shape:\n" + str(data.shape) + "\n"  # returns the dimensions (rows, columns) of the DataFrame as a
    # tuple
    info_str += str(data.info()) + "\n"  # provides information about the DataFrame
    info_str += "Describe:\n" + str(data.describe()) + "\n"  # provides descriptive statistics about each column in
    # the DataFrame

    return data, info_str

'''''
data, info_str = data_loader()
print(data['FastingBS'])
'''