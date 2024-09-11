import tkinter as tk
import random
import string
from tkinter import messagebox

# Function to generate a password based on user input
def generate_password():
    try:
        length = int(length_entry.get())  # Get the desired password length
        if length < 1:
            messagebox.showerror("Input Error", "Password length must be greater than 0")
            return
        
        # Character sets for password generation
        characters = string.ascii_letters  # a-z, A-Z
        if include_numbers.get():
            characters += string.digits  # 0-9
        if include_special.get():
            characters += string.punctuation  # Special characters

        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))

        # Display the password
        password_label.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for password length")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# GUI components
length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12))
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Checkbox for including numbers
include_numbers = tk.BooleanVar()
numbers_checkbox = tk.Checkbutton(root, text="Include Numbers (0-9)", variable=include_numbers)
numbers_checkbox.pack(pady=5)

# Checkbox for including special characters
include_special = tk.BooleanVar()
special_checkbox = tk.Checkbutton(root, text="Include Special Characters (!, @, #, etc.)", variable=include_special)
special_checkbox.pack(pady=5)

# Button to trigger password generation
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
password_label = tk.Label(root, text="", font=("Arial", 14))
password_label.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
