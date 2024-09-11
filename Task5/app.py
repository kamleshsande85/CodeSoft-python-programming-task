import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize an empty contact dictionary
contacts = {}

# Function to add a new contact
def add_contact():
    name = simpledialog.askstring("Input", "Enter Name:")
    phone = simpledialog.askstring("Input", "Enter Phone Number:")
    email = simpledialog.askstring("Input", "Enter Email:")
    address = simpledialog.askstring("Input", "Enter Address:")
    
    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        update_contact_list()
    else:
        messagebox.showerror("Input Error", "Name and Phone are required!")

# Function to update the contact list
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {details['Phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get()
    search_results.delete(0, tk.END)
    
    if search_term:
        found = False
        for name, details in contacts.items():
            if search_term.lower() in name.lower() or search_term in details['Phone']:
                found = True
                search_results.insert(tk.END, f"{name} - {details['Phone']}")
        
        if not found:
            messagebox.showinfo("Search", "No contact found.")
    else:
        messagebox.showerror("Input Error", "Please enter a name or phone number to search.")

# Function to view details of a selected contact
def view_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        details = contacts.get(name, None)
        if details:
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")
    else:
        messagebox.showerror("Selection Error", "Please select a contact to view.")

# Function to update an existing contact
def update_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        details = contacts.get(name, None)
        if details:
            phone = simpledialog.askstring("Update", "Enter new Phone Number:", initialvalue=details['Phone'])
            email = simpledialog.askstring("Update", "Enter new Email:", initialvalue=details['Email'])
            address = simpledialog.askstring("Update", "Enter new Address:", initialvalue=details['Address'])
            
            if phone:
                contacts[name] = {"Phone": phone, "Email": email, "Address": address}
                update_contact_list()
            else:
                messagebox.showerror("Input Error", "Phone number cannot be empty.")
    else:
        messagebox.showerror("Selection Error", "Please select a contact to update.")

# Function to delete a contact
def delete_contact():
    selected_contact = contact_listbox.get(tk.ACTIVE)
    if selected_contact:
        name = selected_contact.split(" - ")[0]
        if name in contacts:
            del contacts[name]
            update_contact_list()
            messagebox.showinfo("Delete", f"Deleted contact: {name}")
    else:
        messagebox.showerror("Selection Error", "Please select a contact to delete.")

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")

# Add Contact Button
add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack(pady=5)

# Contact List
contact_listbox = tk.Listbox(root, height=10, width=40)
contact_listbox.pack(pady=5)

# View Contact Button
view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.pack(pady=5)

# Update Contact Button
update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack(pady=5)

# Delete Contact Button
delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack(pady=5)

# Search Field and Button
search_label = tk.Label(root, text="Search Contact by Name or Phone:")
search_label.pack(pady=5)

search_entry = tk.Entry(root)
search_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack(pady=5)

# Search Results
search_results = tk.Listbox(root, height=5, width=40)
search_results.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
