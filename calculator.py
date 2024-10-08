import tkinter as tk
import math

# Creating a window
root = tk.Tk()
root.title("Advanced Calculator")

# A variable for storing a number in memory
memory = 0

# Creating a widget to display input/output
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


# A function for handling button presses
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


def button_clear():
    entry.delete(0, tk.END)


def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_modulo():
    try:
        number = float(entry.get())
        result = number % 2
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_memory_store():
    global memory
    memory = float(entry.get())


def button_memory_recall():
    entry.delete(0, tk.END)
    entry.insert(0, memory)


def button_memory_clear():
    global memory
    memory = 0


def button_negate():
    try:
        number = float(entry.get())
        result = -number
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_sqrt():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_power():
    try:
        base = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, base)
        entry.insert(tk.END, '**')
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_factorial():
    try:
        number = int(entry.get())
        result = math.factorial(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_log():
    try:
        number = float(entry.get())
        result = math.log10(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_exp():
    try:
        number = float(entry.get())
        result = math.exp(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_sin():
    try:
        number = math.radians(float(entry.get()))
        result = math.sin(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_cos():
    try:
        number = math.radians(float(entry.get()))
        result = math.cos(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


def button_tan():
    try:
        number = math.radians(float(entry.get()))
        result = math.tan(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Creating buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('C', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('%', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('√', 3, 4),
    ('0', 4, 0), ('.', 4, 1), ('/', 4, 2), ('^', 4, 3), ('=', 4, 4),
    ('M+', 5, 0), ('MR', 5, 1), ('MC', 5, 2), ('+/-', 5, 3), ('!', 5, 4),
    ('log', 6, 0), ('exp', 6, 1), ('sin', 6, 2), ('cos', 6, 3), ('tan', 6, 4)
]

# Sorting buttons and creating them on a window with stylization
for button in buttons:
    btn_text, row, col = button
    btn = tk.Button(root, text=btn_text, padx=20, pady=20, font=('Arial', 14))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    # Assigning appropriate command to each button
    if btn_text == "C":
        btn.config(command=button_clear, bg="red", fg="white")
    elif btn_text == "=":
        btn.config(command=button_equal, bg="blue", fg="white")
    elif btn_text == "%":
        btn.config(command=button_modulo, bg="lightgrey")
    elif btn_text == "M+":
        btn.config(command=button_memory_store, bg="lightgrey")
    elif btn_text == "MR":
        btn.config(command=button_memory_recall, bg="lightgrey")
    elif btn_text == "MC":
        btn.config(command=button_memory_clear, bg="lightgrey")
    elif btn_text == "+/-":
        btn.config(command=button_negate, bg="lightgrey")
    elif btn_text == "√":
        btn.config(command=button_sqrt, bg="lightgrey")
    elif btn_text == "^":
        btn.config(command=button_power, bg="lightgrey")
    elif btn_text == "!":
        btn.config(command=button_factorial, bg="lightgrey")
    elif btn_text == "log":
        btn.config(command=button_log, bg="lightgrey")
    elif btn_text == "exp":
        btn.config(command=button_exp, bg="lightgrey")
    elif btn_text == "sin":
        btn.config(command=button_sin, bg="lightgrey")
    elif btn_text == "cos":
        btn.config(command=button_cos, bg="lightgrey")
    elif btn_text == "tan":
        btn.config(command=button_tan, bg="lightgrey")
    else:
        btn.config(command=lambda number=btn_text: button_click(number), bg="lightgrey")

for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
