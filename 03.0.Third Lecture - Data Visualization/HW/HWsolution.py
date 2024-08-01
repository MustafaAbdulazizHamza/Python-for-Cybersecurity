import csv
import matplotlib.pyplot as plt
class Solution:
    def __init__(self, csv_file):
        f = open(csv_file, 'r')
        reader = csv.reader(f)
        self.data = {}
        for crime in reader:
            if crime != []:
                if crime[1] not in self.data.keys():
                    self.data[crime[1]] = 0
                self.data[crime[1]] += 1
        f.close()
    def Visualize(self):
        plt.pie(self.data.values(),labels=self.data.keys(), autopct="%1.1f%%")
        plt.show()
sol = Solution("crimes.csv")
sol.Visualize()


