# This is a sample Python script.
# Mansoor Haidari
# Kelvin Luk
# Korie Westbrook
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("Hi")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Read File Io---------------------------------------------------------------------------------------------
with open('../MedicalAI/cardio_training10Set.csv', 'r') as f:
    # skip the header line
    next(f)
    data = []
    for line in f:
        # split the line into a list of values
        values = line.strip().split(';')
        # convert the values to the appropriate data type
        id_, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio = (
            int(values[0]), int(values[1]), int(values[2]), int(values[3]), float(values[4]), int(values[5]),
            int(values[6]), int(values[7]), int(values[8]), int(values[9]), int(values[10]), int(values[11]),
            int(values[12]))
        # store the values in a nested list
        data.append([id_, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio])

# print the first 5 rows of data
    print("   id_, age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active, cardio")
for row in data[:5]:
    print(row)



# Read File Io---------------------------------------------------------------------------------------------
# Mansoor Haidari
import pandas as pd

# Open the CSV file for reading
with open('heart.csv', 'r') as f:

    # Read lines from file
    lines = f.readlines()

    # Remove newline characters from lines
    lines = [line.strip() for line in lines]

    # Split lines into fields
    fields = [line.split(';') for line in lines]

# Create a pandas DataFrame from the fields
df = pd.DataFrame(fields[1:], columns=fields[0])

# Sort the DataFrame by a category
sorted_df = df.sort_values(by='category')

# Identify the high and low values for a specified column
column_name = 'column_name'
low_value = sorted_df[column_name].min()
high_value = sorted_df[column_name].max()

# Identify the number of 'normal' and 'ST' values in a different column
count_normal = sorted_df[sorted_df['other_column'] == 'normal'].shape[0]
count_st = sorted_df[sorted_df['other_column'] == 'ST'].shape[0]

# Loop through every value in the sorted DataFrame and print it
for index, row in sorted_df.iterrows():
    for col in sorted_df.columns:
        print(row[col])

print('Lowest', column_name, ':', low_value)
print('Highest', column_name, ':', high_value)
print('Number of normal:', count_normal)
print('Number of ST:', count_st)
