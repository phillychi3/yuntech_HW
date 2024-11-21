import tkinter as tk
import time
import math


class AnalogClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clock")

        self.width = 500
        self.height = 500
        self.center_x = self.width // 2
        self.center_y = self.height // 2
        self.clock_radius = min(self.width, self.height) // 2 - 50

        self.canvas = tk.Canvas(
            self.root, width=self.width, height=self.height, background="white"
        )
        self.canvas.pack(expand=True)

        self.draw_clock_face()

        self.update_clock()

    def draw_clock_face(self):
        self.canvas.create_oval(
            self.center_x - self.clock_radius,
            self.center_y - self.clock_radius,
            self.center_x + self.clock_radius,
            self.center_y + self.clock_radius,
            width=2,
            outline="#2980b9",
        )

        for i in range(1, 13):
            angle = i * math.pi / 6 - math.pi / 2
            x = self.center_x + (self.clock_radius - 30) * math.cos(angle)
            y = self.center_y + (self.clock_radius - 30) * math.sin(angle)
            self.canvas.create_text(x, y, text=str(i), font=("Arial", 14, "bold"))

    def draw_hands(self):
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        hour_angle = (hours + minutes / 60) * math.pi / 6 - math.pi / 2
        minute_angle = (minutes + seconds / 60) * math.pi / 30 - math.pi / 2
        second_angle = seconds * math.pi / 30 - math.pi / 2

        self.canvas.delete("hands")

        hour_length = self.clock_radius * 0.5
        hour_x = self.center_x + hour_length * math.cos(hour_angle)
        hour_y = self.center_y + hour_length * math.sin(hour_angle)
        self.canvas.create_line(
            self.center_x,
            self.center_y,
            hour_x,
            hour_y,
            width=6,
            fill="#2c3e50",
            tags="hands",
        )

        minute_length = self.clock_radius * 0.7
        minute_x = self.center_x + minute_length * math.cos(minute_angle)
        minute_y = self.center_y + minute_length * math.sin(minute_angle)
        self.canvas.create_line(
            self.center_x,
            self.center_y,
            minute_x,
            minute_y,
            width=4,
            fill="#3498db",
            tags="hands",
        )

        second_length = self.clock_radius * 0.85
        second_x = self.center_x + second_length * math.cos(second_angle)
        second_y = self.center_y + second_length * math.sin(second_angle)
        self.canvas.create_line(
            self.center_x,
            self.center_y,
            second_x,
            second_y,
            width=2,
            fill="#d63031",
            tags="hands",
        )

        self.canvas.create_oval(
            self.center_x - 8,
            self.center_y - 8,
            self.center_x + 8,
            self.center_y + 8,
            fill="#2c3e50",
            tags="hands",
        )

    def update_clock(self):
        self.draw_hands()
        self.root.after(1000, self.update_clock)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    clock = AnalogClock()
    clock.run()
