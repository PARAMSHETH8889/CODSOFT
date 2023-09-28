import tkinter as tk

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    contact = {"name": name, "phone": phone, "email": email, "address": address}
    contacts.append(contact)
    update_listbox()
    clear_entries()

def update_contact():
    selected = contact_listbox.curselection()
    if selected:
        name = name_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        if name and phone and email and address:
            contact = contacts[selected[0]]
            contact["name"] = name
            contact["phone"] = phone
            contact["email"] = email
            contact["address"] = address
            update_listbox()
            clear_entries()

def delete_contact():
    selected = contact_listbox.curselection()
    if selected:
        contacts.pop(selected[0])
        update_listbox()
        clear_entries()

def search_contact():
    search = search_entry.get()
    if search:
        search_results = []
        for contact in contacts:
            if search.lower() in contact["name"].lower() or search.lower() in contact["phone"].lower() or search.lower() in contact["email"].lower() or search.lower() in contact["address"].lower():
                search_results.append(contact)
        contact_listbox.delete(0, tk.END)
        for contact in search_results:
            contact_listbox.insert(tk.END, contact["name"])

def view_contact():
    selected = contact_listbox.curselection()
    if selected:
        contact = contacts[selected[0]]
        name_entry.delete(0, tk.END)
        name_entry.insert(0, contact["name"])
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["address"])

def update_listbox():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, contact["name"])

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("Contact Book")

# Create the input fields
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

phone_label = tk.Label(root, text="Phone:")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

address_label = tk.Label(root, text="Address:")
address_label.grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=5, pady=5)

# Create the buttons
add_button = tk.Button(root, text="Add", command=add_contact)
add_button.grid(row=4, column=0, padx=5, pady=5)

update_button = tk.Button(root, text="Update", command=update_contact)
update_button.grid(row=4, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete", command=delete_contact)
delete_button.grid(row=4, column=2, padx=5, pady=5)

search_label = tk.Label(root, text="Search:")
search_label.grid(row=5, column=0, padx=5, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=5, column=1, padx=5, pady=5)
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=5, column=2, padx=5, pady=5)

# Create the listbox
contact_listbox = tk.Listbox(root)
contact_listbox.grid(row=6, column=0, columnspan=3, padx=5, pady=5)
update_listbox()

# Create the view fields
view_label = tk.Label(root, text="View Contact:")
view_label.grid(row=7, column=0, padx=5, pady=5)
view_button = tk.Button(root, text="View", command=view_contact)
view_button.grid(row=7, column=1, padx=5, pady=5)

# Run the GUI
root.mainloop()