import tkinter as tk

# Create a window
root = tk.Tk()
root.title("To-Do List")

# Create a listbox to display the tasks
tasks = tk.Listbox(root, width=50)
tasks.pack(pady=10)

# Create an entry widget to add new tasks
new_task = tk.Entry(root, width=50)
new_task.pack(pady=10)

# Define button click functions
def add_task():
    task = new_task.get()
    if task != "":
        tasks.insert(tk.END, task)
        new_task.delete(0, tk.END)

def update_task():
    selected_task = tasks.curselection()
    if selected_task:
        task = new_task.get()
        tasks.delete(selected_task)
        tasks.insert(selected_task, task)
        new_task.delete(0, tk.END)

def delete_task():
    selected_task = tasks.curselection()
    if selected_task:
        tasks.delete(selected_task)

# Create buttons to add, update, and delete tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=10)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# Run the window
root.mainloop()