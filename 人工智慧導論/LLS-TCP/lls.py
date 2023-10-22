import csv
import matplotlib.pyplot as plt
import numpy as np
import copy

class LLS:
    def __init__(self) -> None:
        with open('data.csv', 'r', encoding="utf8") as f:
            data = list(csv.reader(f, delimiter=','))
        self.citys = np.array(data)
        self.citys = self.citys[:, 1:].astype(float)
        np.random.shuffle(self.citys)

    def get_distance(self, cyts=None):
        distance = 0
        if cyts is None:
            for i in range(self.citys.shape[0] - 1):
                distance += np.sqrt((self.citys[i][0] - self.citys[i + 1][0])**2 + (self.citys[i][1] - self.citys[i + 1][1])**2)
        else:
            for i in range(cyts.shape[0] - 1):
                distance += np.sqrt((cyts[i][0] - cyts[i + 1][0])**2 + (cyts[i][1] - cyts[i + 1][1])**2)
        return distance

    def run(self, max_iterations=500):
        mm = max_iterations
        plt.ion()
        plt.figure()
        plt.title('TSP')
        plt.scatter(self.citys[:, 0], self.citys[:, 1])
        plt.plot(self.citys[:, 0], self.citys[:, 1])
        plt.show()
        plt.pause(0.01)

        while max_iterations > 0:
            max_iterations -= 1
            current_tour = copy.deepcopy(self.citys)
            np.random.shuffle(current_tour)
            current_distance = self.get_distance(current_tour)

            improved = True
            while improved:
                improved = False
                for i in range(current_tour.shape[0] - 1):
                    for j in range(i + 2, current_tour.shape[0] - 1):
                        new_tour = copy.deepcopy(current_tour)
                        new_tour[i + 1:j + 1] = new_tour[i + 1:j + 1][::-1]
                        new_distance = self.get_distance(new_tour)

                        if new_distance < current_distance:
                            current_tour = new_tour
                            current_distance = new_distance
                            improved = True

            if current_distance < self.get_distance(self.citys):
                self.citys = current_tour
            plt.clf()
            plt.title(f'TSP - Iteration {mm - max_iterations}')
            plt.plot(current_tour[:, 0], current_tour[:, 1])
            plt.scatter(current_tour[:, 0], current_tour[:, 1])
            plt.pause(0.001)
            print(f'Iteration {mm - max_iterations} - Distance: {current_distance}')

        plt.ioff()
        plt.show()

LLS().run()