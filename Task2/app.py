import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x300")

# Function to perform calculations
def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid Operation")
            return

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# GUI Layout

# Labels and Entry widgets for number inputs
label1 = tk.Label(root, text="Enter First Number:", font=("Arial", 12))
label1.pack(pady=10)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter Second Number:", font=("Arial", 12))
label2.pack(pady=10)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

# Dropdown for selecting operation
operation_var = tk.StringVar(root)
operation_var.set("+")  # Default operation
operation_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/")
operation_menu.pack(pady=10)

# Calculate button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.pack(pady=10)

# Label to display result
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
