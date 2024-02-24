import tkinter as tk

# Створення вікна
root = tk.Tk()
root.title("Калькулятор")

# Змінна для зберігання числа в пам'яті
memory = 0

# Створення віджету для відображення введення/виведення
entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 16))
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)  # розміщуємо віджет на вікні

# Функція для обробки натискання на кнопки
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
        result = number ** 0.5
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
        entry.insert(tk.END, '^')
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Створення кнопок
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('/', 4, 2),
    ('Clear', 4, 3), ('=', 5, 3),
    ('%', 5, 0), ('√', 5, 1), ('x^y', 5, 2),
    ('M+', 6, 0), ('MR', 6, 1), ('MC', 6, 2), ('+/-', 6, 3)
]

# Перебір кнопок і створення їх на вікні зі стилізацією
for button in buttons:
    btn_text, row, col = button
    btn = tk.Button(root, text=btn_text, padx=20, pady=20, font=('Arial', 14))
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    if btn_text == "Clear":
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
    elif btn_text == "x^y":
        btn.config(command=button_power, bg="lightgrey")
    else:
        btn.config(command=lambda number=btn_text: button_click(number), bg="lightgrey")

# Задаємо однакову вагу для всіх рядків і стовпців, щоб кнопки рівномірно розподілялися по вікну
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(5):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
