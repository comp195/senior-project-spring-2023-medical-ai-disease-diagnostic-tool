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
with open('../MedicalAI/Cardio_training10Set.csv', 'r') as f:
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

# print the first number of rows of data
    print("   Age,Sex,ChestPainType,RestingBP,Cholesterol,FastingBS,RestingECG,MaxHR,ExerciseAngina,Oldpeak,ST_Slope,HeartDisease")
for row in data[:10]:
    print(row)
