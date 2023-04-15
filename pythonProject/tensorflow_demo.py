import numpy as np

from pythonProject.Tensor_model import Data_Model
import pandas as pd

# compare the two

# create a neural network that try to predict heart disease if the have it

model = Data_Model()
data = pd.read_csv("heart_check.csv")
data = model.clean_data(data)
# we drop null values and replace it with the median, we also changed non-integer data to integer
data = data.drop('HeartDisease', axis=1)
# we remove the answer column, so we can emulate data that would come from the website.
prediction = model.predict_with_model(data)
print(prediction)