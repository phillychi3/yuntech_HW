import tkinter as tk

def show_name():
    name = entry.get()
    result_label.config(text=f"Hello, {name}!")

def clear_input():
    entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Welcome App")


welcome_label = tk.Label(root, text="Welcome! Please enter your name:")
entry = tk.Entry(root)
show_button = tk.Button(root, text="Show Name", command=show_name)
clear_button = tk.Button(root, text="Clear", command=clear_input)
result_label = tk.Label(root, text="")


welcome_label.grid(row=0, column=0, columnspan=2)
entry.grid(row=1, column=0, columnspan=2)
show_button.grid(row=2, column=0)
clear_button.grid(row=2, column=1)
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()