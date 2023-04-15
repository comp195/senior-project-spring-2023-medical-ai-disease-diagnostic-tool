import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


class MyApp:
    def __init__(self, master):
        self.master = master
        master.title("My App")
        self.master.geometry('600x500')

        self.label = tk.Label(master, text="Select Feature Set:")
        self.label.pack()

        self.feature_set = tk.StringVar(value='all_features')
        self.feature_set_options = ['all_features', 'corr_features', 'chi_features', 'rfe_features']
        self.feature_set_menu = tk.OptionMenu(master, self.feature_set, *self.feature_set_options)
        self.feature_set_menu.pack()

        self.button = tk.Button(master, text="Get Accuracy", command=self.display_accuracy)
        self.button.pack()

        self.figure_canvas = None

    def display_accuracy(self):
        processed_data = pd.read_csv('processed_data.csv')
        corr_features = pd.read_csv('corr_features.csv', header=None).iloc[:, 0].tolist()
        chi2_features = pd.read_csv('chi2_features.csv', header=None).iloc[:, 0].tolist()
        rfe_features = pd.read_csv('rfe_features.csv', header=None).iloc[:, 0].tolist()
        feature_sets = {
            'all_features': processed_data.drop('HeartDisease', axis=1).columns.tolist(),
            'corr_features': corr_features,
            'chi_features': chi2_features,
            'rfe_features': rfe_features,
        }

        features = feature_sets[self.feature_set.get()]
        X = processed_data[features]
        y = processed_data['HeartDisease']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)

        if self.figure_canvas:
            self.figure_canvas.get_tk_widget().pack_forget()

        fig, ax = plt.subplots(figsize=(4, 4))
        ax.bar(['Accuracy'], [accuracy])
        ax.set_ylim([0, 1])
        ax.set_title(f'Accuracy for {self.feature_set.get()}')
        ax.set_ylabel('Accuracy')
        self.figure_canvas = FigureCanvasTkAgg(fig, master=self.master)
        self.figure_canvas.get_tk_widget().pack()



if __name__ == '__main__':
    root = tk.Tk()
    myapp = MyApp(root)
    root.mainloop()
