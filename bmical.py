import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

users_data = {}

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = weight / (height ** 2)
    bmi_result_label.config(text="Your BMI is: {:.2f}".format(bmi))
    bmi_category = classify_bmi(bmi)
    bmi_category_label.config(text="You are " + bmi_category)
    save_user_data(weight, height, bmi)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_user_data(weight, height, bmi):
    user_id = user_id_entry.get()
    if user_id in users_data:
        users_data[user_id].append((weight, height, bmi))
    else:
        users_data[user_id] = [(weight, height, bmi)]
    messagebox.showinfo("Success", "Data saved successfully for user " + user_id)

def view_historical_data():
    user_id = user_id_entry.get()
    if user_id in users_data:
        data = users_data[user_id]
        data_str = "Historical data for user " + user_id + ":\n"
        for entry in data:
            data_str += "Weight: {:.2f} kg, Height: {:.2f} m, BMI: {:.2f}\n".format(entry[0], entry[1], entry[2])
        messagebox.showinfo("Historical Data", data_str)
    else:
        messagebox.showinfo("Error", "User ID does not exist")

def plot_bmi_trend():
    user_id = user_id_entry.get()
    if user_id in users_data:
        data = users_data[user_id]
        weights = [entry[0] for entry in data]
        heights = [entry[1] for entry in data]
        bmis = [entry[2] for entry in data]
        plt.plot(weights, label='Weight (kg)')
        plt.plot(heights, label='Height (m)')
        plt.plot(bmis, label='BMI')
        plt.xlabel('Recorded Data')
        plt.ylabel('Value')
        plt.title('BMI Trend Analysis')
        plt.legend()
        plt.show()
    else:
        messagebox.showinfo("Error", "User ID does not exist")

root = tk.Tk()
root.title("BMI Calculator & Analysis")

user_id_label = tk.Label(root, text="Enter User ID:")
user_id_label.pack()
user_id_entry = tk.Entry(root)
user_id_entry.pack()

weight_label = tk.Label(root, text="Enter your weight in kilograms:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

height_label = tk.Label(root, text="Enter your height in meters:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

historical_data_button = tk.Button(root, text="View Historical Data", command=view_historical_data)
historical_data_button.pack()

plot_bmi_trend_button = tk.Button(root, text="Plot BMI Trend", command=plot_bmi_trend)
plot_bmi_trend_button.pack()

bmi_result_label = tk.Label(root, text="")
bmi_result_label.pack()

bmi_category_label = tk.Label(root, text="")
bmi_category_label.pack()

root.mainloop()
