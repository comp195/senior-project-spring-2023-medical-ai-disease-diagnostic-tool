

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