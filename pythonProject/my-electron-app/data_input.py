import logging
import pickle
import pandas as pd
from data_preprocess import data_preprocess
from data_model import feature_sets
import sys
import json


def make_predictions(age, sex, chestPainType, restingBP, cholesterol, fastingBS, restingECG, maxHR, exerciseAngina,
                     oldpeak, stSlope):
    original_data = pd.read_csv('heart.csv')


    logging.basicConfig(filename="std.log",
                        format='%(asctime)s %(message)s',
                        filemode='w')

    # Let us Create an object
    logger = logging.getLogger()

    # Now we are going to Set the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    # some messages to test
    logger.debug("This is just a harmless debug message")
    logger.info("This is just an information for you")
    logger.warning("OOPS!!!Its a Warning")
    logger.error("Have you try to divide a number by zero")
    logger.critical("The Internet is not working....")
    # Create a dictionary containing the input data
    original_input_data = {
        'Age': age,
        'Sex': sex,
        'ChestPainType': chestPainType,
        'RestingBP': restingBP,
        'Cholesterol': cholesterol,
        'FastingBS': fastingBS,
        'RestingECG': restingECG,
        'MaxHR': maxHR,
        'ExerciseAngina': exerciseAngina,
        'Oldpeak': oldpeak,
        'ST_Slope': stSlope,
    }
    logger.info(original_input_data)

    # Convert the input data to a pandas DataFrame with an explicit index
    original_input_df = pd.DataFrame([original_input_data])


    # Preprocess the input data using the same techniques used in the model
    preprocessed_input_df, fitted_scaler = data_preprocess(original_input_df, mode='prediction')
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        logger.info(preprocessed_input_df)

    processed_data = pd.read_csv('processed_data.csv')
    processed_data = processed_data.drop(columns=['HeartDisease'])
    missing_columns = set(processed_data.columns) - set(preprocessed_input_df.columns)
    for col in missing_columns:
        preprocessed_input_df[col] = 0

    preprocessed_input_df = preprocessed_input_df[processed_data.columns]

    #input_df = []
    #for col in preprocessed_input_df.columns:
    #    input_df[col] = preprocessed_input_df.at[0, col]

    # Load the trained model
    models = {}
    with open('Logistic Regression.pkl', 'rb') as f:
        models['Logistic Regression'] = pickle.load(f)
    with open('Random Forest.pkl', 'rb') as f:
        models['Random Forest'] = pickle.load(f)
    with open('Naive Bayes.pkl', 'rb') as f:
        models['Naive Bayes'] = pickle.load(f)

    # Use the model to make predictions on the input data
    predictions = {}
    for name, model in models.items():
        #print(name)
        #print(model.feature_names_in_)
        y_pred = model.predict_proba(preprocessed_input_df)
        predictions[name] = y_pred[0].tolist()

    # Return the predicted outcome
    return predictions


data_string = sys.argv[1]

#data_string = '{"age":40,"sex":"male","chestPainType":"atypical-angina","restingBP":140,"cholesterol":289,"fastingBS":0,"restingECG":"normal","maxHR":172,"exerciseAngina":0,"oldpeak":0,"stSlope":"up-sloping"}'
data = json.loads(data_string)
predictions = make_predictions(**data)
print(json.dumps(predictions))



'''


print("Welcome to the Heart Disease Risk Assessment Tool.")
print("Please answer the following questions to help us assess your risk.")

# Get user input
while True:
    try:
        age = int(input("Enter your age: "))
        if age < 0 or age > 112:
            print("Please enter a valid age between 0 and 112.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer age.")

while True:
    sex = input("Enter your sex (male/female): ")
    if sex.lower() not in ['male', 'female', 'm', 'f']:
        print("Please enter either 'male' or 'female'.")
        continue
    break

while True:
    illness = input("Do you have an existing medical condition? (yes/no): ")
    if illness.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    exercise = input("Do you exercise regularly? (yes/no): ")
    if exercise.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    try:
        cholesterol = int(input("What is your cholesterol level? "))
        if cholesterol < 0:
            print("Please enter a valid cholesterol level.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer cholesterol level.")

while True:
    chest_pain = input("Do you experience chest pain? (yes/no): ")
    if chest_pain.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    try:
        blood_pressure = int(input("What is your blood pressure? "))
        if blood_pressure < 0:
            print("Please enter a valid blood pressure.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer blood pressure.")

while True:
    marital_status = input("What is your marital status? (married/single): ")
    if marital_status.lower() not in ['married', 'single', 'm', 's']:
        print("Please enter either 'married' or 'single'.")
        continue
    break

while True:
    medical_history = input("Do you have a family history of heart disease? (yes/no): ")
    if medical_history.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    symptoms = input("Have you experienced any of the following symptoms? (shortness of breath when active, trouble breathing when sleeping): ")
    if symptoms.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")

        continue
    break

# Additional medical history questions
while True:
    heart_attack = input("Have you ever had a heart attack or stroke? (yes/no): ")
    if heart_attack.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    diabetes = input("Do you have diabetes? (yes/no): ")
    if diabetes.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    high_bp = input("Have you ever been diagnosed with high blood pressure? (yes/no): ")
    if high_bp.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

    high_chol = input("Have you ever been diagnosed with high cholesterol? (yes/no): ")
    if high_chol.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    arrhythmia = input("Have you ever been diagnosed with a heart arrhythmia or irregular heartbeat? (yes/no): ")
    if arrhythmia.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    heart_valve = input("Have you ever been diagnosed with heart valve disease? (yes/no): ")
    if heart_valve.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
  cong_heart_defect = input("Have you ever been diagnosed with a congenital heart defect? (yes/no): ")
  if cong_heart_defect.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
  break

while True:
    PAD = input("Have you ever been diagnosed with peripheral artery disease (PAD)? (yes/no): ")
    if PAD.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    blood_clot = input("Have you ever been diagnosed with a blood clotting disorder? (yes/no): ")
    if blood_clot.lower() not in ['yes', 'no', 'y', 'n']:
        print("Please enter either 'yes' or 'no'.")
        continue
    break

while True:
    sleep_apnea = input("Have you ever been diagnosed with sleep apnea or other breathing problems during sleep? (yes/no): ")
    if sleep_apnea.lower() not in ['yes', 'no', 'y', 'n']:
      print("Please enter either 'yes' or 'no'.")
      continue
    break


# Analyze heart disease risk factors
age_risk = "Moderate Risk" if (sex == ("male" or 'm') and age > 45) or (sex == ("female" or 'f' )and age > 55) else "Low Risk"
sex_risk = "High Risk" if sex == ("male" or "m") else "No Risk"
illness_risk = "High Risk" if illness == ("yes" or 'y') else "No Risk"
exercise_risk = "No Risk" if exercise == ("yes"  or 'y') else "High Risk"
if cholesterol < 200:
    chol_risk = "Low Risk"
elif cholesterol >= 200 and cholesterol <= 239:
    chol_risk = "Moderate Risk"
else:
    chol_risk = "High Risk"

# determine the risk of chest pain based on the user input
chest_pain_risk = "High Risk" if chest_pain == ("yes" or 'y') else "Low Risk"

# print out the risk analysis chart
print("\nRisk Analysis Chart:")
print(f"Age: {age_risk}")
print(f"Sex: {sex_risk}")
print(f"Exercise: {exercise_risk}")
print(f"Chest Pain: {chest_pain_risk}")

# suggest seeing a doctor based on the risk assessment
if age >= 50 or sex == "male" or illness == ("yes" or "y") or exercise == ("no" or 'n') or cholesterol >= 240 or chest_pain ==  ("yes" or "y") or blood_pressure >= 140:
    print("\nBased on your risk assessment, we suggest that you see a doctor for further evaluation.")
else:
    print("\nYour risk of developing heart disease is low, but we still recommend that you maintain a healthy lifestyle and visit a doctor regularly for checkups.")

'''
