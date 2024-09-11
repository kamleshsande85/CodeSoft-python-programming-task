import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Global task list
tasks = []

# Function to update the displayed task list
def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "✓" if task["completed"] else "✗"
        task_listbox.insert(tk.END, f"{i+1}. {task['description']} [{status}]")

# Add Task Function
def add_task():
    task_desc = task_entry.get()
    if task_desc == "":
        messagebox.showwarning("Input Error", "Task description cannot be empty!")
        return
    task = {"description": task_desc, "completed": False}
    tasks.append(task)
    update_task_list()
    task_entry.delete(0, tk.END)

# Mark Task as Completed
def complete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as complete!")

# Delete Task Function
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")

# GUI Layout
task_label = tk.Label(root, text="Task Description:", font=("Arial", 12))
task_label.pack(pady=10)

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Mark as Completed", width=15, command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
