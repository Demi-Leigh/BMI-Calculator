# Designing a program that calculates your BMI
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

# Creating a window
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("500x300")
window.resizable(0, 0)


# Creating labels and entry boxes for Height
height_label = tk.Label(text="Height: ")
height_label.grid(row=0, column=0, pady=20, padx=20)
cm_label = tk.Label(text="cm")
cm_label.grid(row=0, column=2)
Height = tk.StringVar()
height_ent = tk.Entry(width=10, bg="grey", textvariable=Height)
height_ent.grid(row=0, column=1)


# Creating labels and entry boxes for Weight
weight_label = tk.Label(text="Weight: ")
weight_label.grid(row=1, column=0)
kg_label = tk.Label(text="Kilograms")
kg_label.grid(row=1, column=2)
Weight = tk.StringVar()
weight_ent = tk.Entry(width=10, bg="grey", textvariable=Weight)
weight_ent.grid(row=1, column=1)

# Creating option menu for gender
gender_label = tk.Label(text="Gender: ")
gender_label.grid(row=3, column=0)
Gender = tk.StringVar()
gender_box = ttk.Combobox(window, width=10, textvariable="Gender", state="readonly")
gender_box["values"] = "Select Male Female"
gender_box.current(0)
gender_box.grid(row=3, column=1, pady=10)

# Creating label and entry for Age
age_label = tk.Label(text="Age: ")
age_label.grid(row=4, column=0, pady=10)
Age = tk.StringVar()
age_ent = tk.Entry(window, width=10, bg="grey", textvariable="Age")
age_ent.grid(row=4, column=1)


# Creating the Calculate,Exit and Clear buttons
ans_btn = tk.Button(text="Calculate", command="calculate_bmi", bg="grey")
ans_btn.grid(row=5, column=0, padx=10, pady=20)

clear_btn = tk.Button(text="Clear", command="clear", bg="grey")
clear_btn.grid(row=5, column=1, padx=10, pady=20)

exit_btn = tk.Button(text="Exit", command="exit", bg="grey")
exit_btn.grid(row=5, column=2, padx=10, pady=20)


# Defining functions
def calculate_bmi():
    print(weight_entry.get())
    weight = float(weight_ent.get())
    height = float(height_ent.get())
    answer = weight / (height / 100) ** 2

def ideal_bmi():
     weight = float(weight_ent.get())
     height = float(height_ent.get())
     gender = gender_box.get()


     if gender == "male":
        result = 0.5 * weight / ((height / 100) ** 2) + 11.5
        bmi = round(result, 2)
        print(bmi)











window.mainloop()


