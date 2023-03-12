import pandas as pd
import matplotlib.pyplot as plt
# load data from csv file
df = pd.read_csv('heart.csv')

# plot histograms for each column
plt.hist(df['Age'])
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['Sex'])
plt.title('Sex Distribution')
plt.xlabel('Sex')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['ChestPainType'])
plt.title('Chest Pain Type Distribution')
plt.xlabel('Chest Pain Type')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['RestingBP'])
plt.title('Resting Blood Pressure Distribution')
plt.xlabel('Resting Blood Pressure')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['Cholesterol'])
plt.title('Cholesterol Distribution')
plt.xlabel('Cholesterol')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['FastingBS'])
plt.title('Fasting Blood Sugar Distribution')
plt.xlabel('Fasting Blood Sugar')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['RestingECG'])
plt.title('Resting Electrocardiogram Distribution')
plt.xlabel('Resting Electrocardiogram')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['MaxHR'])
plt.title('Maximum Heart Rate Distribution')
plt.xlabel('Maximum Heart Rate')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['ExerciseAngina'])
plt.title('Exercise-Induced Angina Distribution')
plt.xlabel('Exercise-Induced Angina')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['Oldpeak'])
plt.title('ST Depression Distribution')
plt.xlabel('ST Depression')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['ST_Slope'])
plt.title('ST Slope Distribution')
plt.xlabel('ST Slope')
plt.ylabel('Frequency')
plt.show()

plt.hist(df['HeartDisease'])
plt.title('Heart Disease Distribution')
plt.xlabel('Heart Disease')
plt.ylabel('Frequency')
plt.show()