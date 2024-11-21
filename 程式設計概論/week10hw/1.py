import tkinter as tk
from time import strftime

class DigitalClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Clock')
        self.root.geometry('400x150')
        self.root.configure(bg='black')
        self.clock_label = tk.Label(
            self.root,
            font=('DS-Digital', 60),
            background='black',
            foreground='#27ae60'
        )
        self.clock_label.pack(pady=20)
        self.update_time()

    def update_time(self):
        time_string = strftime('%H:%M:%S')
        self.clock_label.config(text=time_string)
        self.root.after(1000, self.update_time)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    clock = DigitalClock()
    clock.run()