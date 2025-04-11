import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    if name and phone:
        if name in contacts:
            messagebox.showinfo("Duplicate", "Contact already exists.")
        else:
            contacts[name] = phone
            update_contact_list()
            name_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Info", "Please enter both name and phone.")

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected[0]).split(" - ")[0]
        del contacts[name]
        update_contact_list()
    else:
        messagebox.showwarning("No Selection", "Please select a contact to delete.")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, phone in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {phone}")

# GUI Setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("300x400")

tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Contacts:").pack()
contact_listbox = tk.Listbox(root, width=40)
contact_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
