import tkinter as tk
from tkinter import messagebox

def calculate_product():
    try:
        number = int(entry_number.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")
        return
    
    digits = [int(d) for d in str(number) if int(d) % 3 == 0 and int(d) != 0]
    if not digits:
        product = 0
    else:
        if selected_cycle.get() == "for":
            product = 1
            for digit in digits:
                product *= digit
        elif selected_cycle.get() == "while":
            product = 1
            i = 0
            while i < len(digits):
                product *= digits[i]
                i += 1
    
    entry_result.delete(0, tk.END)
    entry_result.insert(0, str(product))

def clear_entries():
    entry_number.delete(0, tk.END)
    entry_result.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Работа с виджетом Radiobutton")

# Create and place the widgets
label_select = tk.Label(root, text="Выберите цикл:")
label_select.grid(row=0, column=0, padx=10, pady=5, sticky="w")

selected_cycle = tk.StringVar(value="for")
radiobutton_for = tk.Radiobutton(root, text="for", variable=selected_cycle, value="for")
radiobutton_for.grid(row=1, column=0, padx=10, pady=5, sticky="w")
radiobutton_while = tk.Radiobutton(root, text="while", variable=selected_cycle, value="while")
radiobutton_while.grid(row=2, column=0, padx=10, pady=5, sticky="w")

label_number = tk.Label(root, text="Введите целое число:")
label_number.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_number = tk.Entry(root)
entry_number.grid(row=4, column=0, padx=10, pady=5, sticky="w")

label_result = tk.Label(root, text="Произведение цифр кратных 3:")
label_result.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_result = tk.Entry(root)
entry_result.grid(row=6, column=0, padx=10, pady=5, sticky="w")

button_calculate = tk.Button(root, text="Вычислить", command=calculate_product)
button_calculate.grid(row=7, column=0, padx=10, pady=5, sticky="w")
button_clear = tk.Button(root, text="Очистить", command=clear_entries)
button_clear.grid(row=7, column=0, padx=90, pady=5, sticky="w")

# Run the application
root.mainloop()
