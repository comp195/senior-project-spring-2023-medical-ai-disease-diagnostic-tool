import matplotlib.pyplot as plt
import pandas as pd

# read data into a pandas dataframe
df = pd.read_csv('heart.csv')

# create a figure with subplots for each column
fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(20, 15))

# loop over each column and plot a histogram
for i, col in enumerate(df.columns):
    ax = axs[i // 4, i % 4]  # select the appropriate subplot
    ax.hist(df[col], bins=20, color='blue', alpha=0.5)  # plot histogram
    ax.set_title(col)  # set the subplot title

# adjust the spacing between subplots
plt.tight_layout()

# show the plot
plt.show()