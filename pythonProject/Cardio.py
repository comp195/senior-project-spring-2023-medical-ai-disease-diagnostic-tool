import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
#import tensorflow as tf
#import keras
import torch
import os

print(os.getcwd())

# load the dataset
data = pd.read_csv('heart.csv', delimiter=',')
print(data.head())

