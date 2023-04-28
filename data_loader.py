import numpy as np
import pandas as pd
import os

#print(os.getcwd(), "\n")

def data_loader():
    """
    Loads the heart.csv dataset, gathers some basic information, and returns the loaded data and the information string.

    Returns:
        tuple: A tuple containing the loaded dataset (as a pandas DataFrame) and an information string with some basic statistics.
    """

    data = pd.read_csv('heart.csv', delimiter=',')
    info_str = ""
    info_str += f"Head:\n{data.head(5)}\n"  # display the first few rows of the DataFrame
    info_str += f"Shape:\n{data.shape}\n"  # returns the dimensions (rows, columns) of the DataFrame as a
    # tuple
    info_str += str(data.info()) + "\n" # provides information about the DataFrame
    info_str += f"Describe:\n{data.describe()}\n"  # provides descriptive statistics about each column in
    # the DataFrame

    return data, info_str

if __name__ == "__main__":
    data, info = data_loader()
