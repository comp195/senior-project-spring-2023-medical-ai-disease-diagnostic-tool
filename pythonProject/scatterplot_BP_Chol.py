import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('heart.csv')

sns.scatterplot(data=df, x='Cholesterol', y='RestingBP', hue='Age', style='Sex', palette='coolwarm')

plt.title('Resting Blood Pressure vs Cholesterol')
plt.xlabel('Cholesterol')
plt.ylabel('Resting Blood Pressure')

plt.show()

