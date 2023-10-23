import csv
import matplotlib.pyplot as plt
import numpy as np
import random
import os


class LLS:
    def __init__(self) -> None:
        path = os.path.dirname(os.path.abspath(__file__))
        with open(path + "./data.csv", "r", encoding="utf8") as f:
            data = list(csv.reader(f, delimiter=","))
        self.city_positions = np.array(data)[:, 1:].astype(float)

    def get_distance(self, wow):
        distance = 0
        for i in range(self.city_positions.shape[0] - 1):
            city1 = wow[i]
            city2 = wow[i + 1]
            x1, y1 = self.city_positions[city1]
            x2, y2 = self.city_positions[city2]
            distance += np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance

    def isbetter(self, new_distance, old_distance):
        return self.get_distance(new_distance) <= self.get_distance(old_distance)

    def two_opt_swap(self, tour, i, j):
        new_tour = tour[:i] + tour[i : j + 1][::-1] + tour[j + 1 :]
        return new_tour

    def randompath(self, path):
        a = np.random.randint(len(path))
        while True:
            b = np.random.randint(len(path))
            if np.abs(a - b) > 1:
                break
        if a > b:
            return b, a
        else:
            return a, b

    def run(self, max_iterations=10000):
        path = list(range(len(self.city_positions)))
        best_path = path
        best_distance = self.get_distance(path)

        while max_iterations > 0:
            i, j = self.randompath(path)
            new_path = self.two_opt_swap(path, i, j)
            new_distance = self.get_distance(new_path)
            if new_distance < best_distance:
                best_path = new_path
                best_distance = new_distance
                print("New best distance:", best_distance)
            max_iterations -= 1

        print("Best Distance:", best_distance)
        print("Best Path:", best_path)

        plt.subplot(111, aspect="equal")
        plt.plot(
            self.city_positions[:, 0], self.city_positions[:, 1], "x", color="blue"
        )
        for i, city in enumerate(self.city_positions):
            plt.text(city[0], city[1], str(i))
        plt.plot(
            self.city_positions[best_path, 0],
            self.city_positions[best_path, 1],
            color="red",
        )
        plt.show()


LLS().run()
