from tkinter import Tk, Button

def show_hello():
    print("Hello, World!")

root = Tk()
root.title("Hello World App")

button = Button(root, text="Press Me", command=show_hello)
button.pack(pady=20)

root.mainloop()