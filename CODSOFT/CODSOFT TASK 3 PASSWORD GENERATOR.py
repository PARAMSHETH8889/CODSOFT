import string
import random
import tkinter as tk

# Define function to generate password
def generate_password():
    length = int(length_entry.get())
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    password_display.config(text=password)

# Create a window
root = tk.Tk()
root.title("Password Generator")

# Create a label and entry widget for password length
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Create a button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Create a label to display the generated password
password_display = tk.Label(root, text="")
password_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Run the window
root.mainloop()