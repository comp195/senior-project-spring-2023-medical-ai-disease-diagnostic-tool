print("Welcome to the Heart Disease Risk Assessment Tool.")
print("Please answer the following questions to help us assess your risk.")

# Get user input
age = int(input("Enter your age: "))
sex = input("Enter your sex (male/female): ")
illness = input("Do you have an existing medical condition? (yes/no): ")
exercise = input("Do you exercise regularly? (yes/no): ")
cholesterol = int(input("What is your cholesterol level? "))
chest_pain = input("Do you experience chest pain? (yes/no): ")
blood_pressure = int(input("What is your blood pressure? "))
marital_status = input("What is your marital status? (married/single): ")
medical_history = input("Do you have a family history of heart disease? (yes/no): ")
symptoms = input("Have you experienced any of the following symptoms? (shortness of breath when active, trouble breathing when sleeping): ")

# Additional medical history questions
heart_attack = input("Have you ever had a heart attack or stroke? (yes/no): ")
diabetes = input("Do you have diabetes? (yes/no): ")
high_bp = input("Have you ever been diagnosed with high blood pressure? (yes/no): ")
high_chol = input("Have you ever been diagnosed with high cholesterol? (yes/no): ")
arrhythmia = input("Have you ever been diagnosed with a heart arrhythmia or irregular heartbeat? (yes/no): ")
heart_valve = input("Have you ever been diagnosed with heart valve disease? (yes/no): ")
cong_heart_defect = input("Have you ever been diagnosed with a congenital heart defect? (yes/no): ")
PAD = input("Have you ever been diagnosed with peripheral artery disease (PAD)? (yes/no): ")
blood_clot = input("Have you ever been diagnosed with a blood clotting disorder? (yes/no): ")
sleep_apnea = input("Have you ever been diagnosed with sleep apnea or other breathing problems during sleep? (yes/no): ")

# Analyze heart disease risk factors
age_risk = "Moderate Risk" if (sex == "male" and age > 45) or (sex == "female" and age > 55) else "Low Risk"
sex_risk = "High Risk" if sex == "male" else "No Risk"
illness_risk = "High Risk" if illness == "yes" else "No Risk"
exercise_risk = "No Risk" if exercise == "yes" else "High Risk"
if cholesterol < 200:
    chol_risk = "Low Risk"
elif cholesterol >= 200 and cholesterol <= 239:
    chol_risk = "Moderate Risk"
else:
    chol_risk = "High Risk"

# determine the risk of chest pain based on the user input
chest_pain_risk = "High Risk" if chest_pain == "yes" else "Low Risk"

# print out the risk analysis chart
print("\nRisk Analysis Chart:")
print(f"Age: {age_risk}")
print(f"Sex: {sex_risk}")
print(f"Exercise: {exercise_risk}")
print(f"Chest Pain: {chest_pain_risk}")

# suggest seeing a doctor based on the risk assessment
if age >= 50 or sex == "male" or illness == "yes" or exercise == "no" or cholesterol >= 240 or chest_pain == "yes" or blood_pressure >= 140:
    print("\nBased on your risk assessment, we suggest that you see a doctor for further evaluation.")
else:
    print("\nYour risk of developing heart disease is low, but we still recommend that you maintain a healthy lifestyle and visit a doctor regularly for checkups.")
