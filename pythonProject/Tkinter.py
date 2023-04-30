from pythonProject.Tensor_model import Data_Model
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt
import numpy as np

# compare the two

# create a neural network that try to predict heart disease if they have it Creates a new window


global sex_var , chest_pain_var, age_entry,model,bp_entry,ch_entry,fbs_entry,ecg_var,mhx_entry,exa_var,op_var,sts_var,out_label,name_entry,address_entry


def model_test ():
    global model
    model = Data_Model()
    data = pd.read_csv("heart_check.csv")
    data = model.clean_data(data)
    # we drop null values and replace it with the median, we also changed non-integer data to integer
    data = data.drop('HeartDisease', axis=1)
    # we remove the answer column, so we can emulate data that would come from the website.
    prediction = model.predict_with_model(data)
    print(prediction)

def submit_form():
    df = pd.DataFrame(columns=["Age","Sex","ChestPainType","RestingBP","Cholesterol","FastingBS","RestingECG","MaxHR","ExerciseAngina","Oldpeak","ST_Slope"])
    age = int(age_entry.get())
    sex = sex_var.get()
    chest_pain = chest_pain_var.get()
    bp = int(bp_entry.get())
    ch = int(ch_entry.get())
    fbs = int(fbs_entry.get())
    ecg = ecg_var.get()
    mhx = int(mhx_entry.get())
    exa = exa_var.get()
    op = float(op_var.get())
    sts = sts_var.get()
    name =name_entry.get()
    address = address_entry.get()



    df = df.append({"Age": age,"Sex": sex,"ChestPainType": chest_pain ,"RestingBP":bp,"Cholesterol":ch,"FastingBS":fbs,"RestingECG":ecg,"MaxHR":mhx,"ExerciseAngina":exa,"Oldpeak":op,"ST_Slope":sts}, ignore_index= True)
    df = model.clean_data(df)
    pd.set_option('display.max_columns', None)
    print(df)
    prediction = model.predict_with_model(df)
    global out_label
    out_label.config(text=prediction)


    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> age:',age,)

def run_demo():
    global model
    model = Data_Model()
    model.plot_stat()
    run_form()


def run_form():
    root = tk.Tk()
    root.title("Medical AI Diagnostic Tool")
    title_label = tk.Label(root, text="Welcome to the Medical AI Diagnostic Tool", font=("Arial", 16, "bold"))
    form_frame = tk.Frame(root)

    # Set the window title

    form_frame.pack(padx=10, pady=10)


    # add patient name label and entry
    name_label = tk.Label(form_frame, text="Patient Name:")
    name_label.grid(row=0, column=0, sticky='w')
    global name_entry
    name_entry = tk.Entry(form_frame)
    name_entry.grid(row=0, column=1)

    # add patient address label and entry
    address_label = tk.Label(form_frame, text="Patient Address:")
    address_label.grid(row=1, column=0, sticky='w')
    global address_entry
    address_entry = tk.Entry(form_frame)
    address_entry.grid(row=1, column=1)

    age_label = tk.Label(form_frame, text="Age:")
    age_label.grid(row=2, column=0, sticky='w')
    global age_entry
    age_entry = tk.Entry(form_frame)
    age_entry.grid(row=2, column=1)

    global sex_var
    sex_label = tk.Label(form_frame, text="Gender:")
    sex_label.grid(row=3, column=0, sticky="w")
    sex_var = tk.StringVar(value='M')
    sex_frame = tk.Frame(form_frame)
    sex_frame.grid(row=3, column=1, sticky="w")
    sex_f_button = tk.Radiobutton(sex_frame, text="Male", variable=sex_var, value="M")
    sex_f_button.pack(side='left')
    sex_m_button = tk.Radiobutton(sex_frame, text="Female", variable=sex_var, value="F")
    sex_m_button.pack(side='left')

    global chest_pain_var
    chest_pain_label = tk.Label(form_frame,text="Chest Pain Level")
    chest_pain_label.grid(row=4,column=0,sticky="w")
    chest_pain_var=tk.StringVar(value="ASY")
    chest_pain_frame = tk.Frame(form_frame)
    chest_pain_frame.grid(row=4, column=1, sticky="w")
    chest_pain_none_button = tk.Radiobutton(chest_pain_frame, text="None", variable=chest_pain_var, value="ASY")
    chest_pain_none_button.pack(side='left')
    chest_pain_low_button = tk.Radiobutton(chest_pain_frame, text="Low", variable=chest_pain_var, value="NAP")
    chest_pain_low_button.pack(side='left')
    chest_pain_medium_button = tk.Radiobutton(chest_pain_frame, text="Medium", variable=chest_pain_var, value="ATA")
    chest_pain_medium_button.pack(side='left')
    chest_pain_high_button = tk.Radiobutton(chest_pain_frame, text="High", variable=chest_pain_var, value="TA")
    chest_pain_high_button.pack(side='left')

    bp_label = tk.Label(form_frame, text="Resting BP:")
    bp_label.grid(row=5, column=0, sticky='w')
    global bp_entry
    bp_entry = tk.Entry(form_frame)
    bp_entry.grid(row=5, column=1)

    ch_label = tk.Label(form_frame, text="Cholesterol:")
    ch_label.grid(row=6, column=0, sticky='w')
    global ch_entry
    ch_entry = tk.Entry(form_frame)
    ch_entry.grid(row=6, column=1)

    fbs_label = tk.Label(form_frame, text="Fasting Blood Suger:")
    fbs_label.grid(row=7, column=0, sticky='w')
    global fbs_entry
    fbs_entry = tk.Entry(form_frame)
    fbs_entry.grid(row=7, column=1)

    global ecg_var
    ecg_label = tk.Label(form_frame, text="Resting ECG:")
    ecg_label.grid(row=8, column=0, sticky="w")
    ecg_var = tk.StringVar(value="Normal")
    ecg_frame = tk.Frame(form_frame)
    ecg_frame.grid(row=8, column=1, sticky="w")
    ecg_f_button = tk.Radiobutton(ecg_frame, text="Normal", variable=ecg_var, value="Normal")
    ecg_f_button.pack(side='left')
    ecg_m_button = tk.Radiobutton(ecg_frame, text="ST", variable=ecg_var, value="ST")
    ecg_m_button.pack(side='left')

    mhx_label = tk.Label(form_frame, text="Max Heart Rate:")
    mhx_label.grid(row=9, column=0, sticky='w')
    global mhx_entry
    mhx_entry = tk.Entry(form_frame)
    mhx_entry.grid(row=9, column=1)

    global exa_var
    exa_label = tk.Label(form_frame, text="Exercise Angina :")
    exa_label.grid(row=10, column=0, sticky="w")
    exa_var = tk.StringVar(value="N")
    exa_frame = tk.Frame(form_frame)
    exa_frame.grid(row=10, column=1, sticky="w")
    exa_f_button = tk.Radiobutton(exa_frame, text="Yes", variable=exa_var, value="Y")
    exa_f_button.pack(side='left')
    exa_button = tk.Radiobutton(exa_frame, text="No", variable=exa_var, value="N")
    exa_button.pack(side='left')

    op_label = tk.Label(form_frame, text="Old Peak:")
    op_label.grid(row=11, column=0, sticky='w')
    global op_var
    op_var = tk.Entry(form_frame)
    op_var.grid(row=11, column=1)

    global sts_var
    sts_label = tk.Label(form_frame, text="ST Slope :")
    sts_label.grid(row=12, column=0, sticky="w")
    sts_var = tk.StringVar(value="Down")
    sts_frame = tk.Frame(form_frame)
    sts_frame.grid(row=12, column=1, sticky="w")
    sts_f_button = tk.Radiobutton(sts_frame, text="Down", variable=sts_var, value="Down")
    sts_f_button.pack(side='left')
    sts_f_button = tk.Radiobutton(sts_frame, text="Flat", variable=sts_var, value="Flat")
    sts_f_button.pack(side='left')
    sts_button = tk.Radiobutton(sts_frame, text="Up", variable=sts_var, value="Up")
    sts_button.pack(side='left')

    submit_button = tk.Button(form_frame, text="Submit", command=submit_form)
    submit_button.grid(row=14,columnspan=2)


    global out_label
    out_label= tk.Label(form_frame)
    out_label.grid(row=14,column=0)


    root.mainloop()



if __name__ == '__main__':
    run_demo()