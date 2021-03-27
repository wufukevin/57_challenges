import RegulationFunction as rf
import math
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class InputData:
    def __init__(self, restingPulse, age):
        self.restingPulse = int(restingPulse)
        self.age = int(age)
        self.data = np.ndarray((9, 2), dtype=object)
        for i in range(9):
            intensity = 55+i*5 # in percentage
            self.data[i][0] = f'{intensity}%'
            self.data[i][1] = f'{self.targetHeartRate(intensity)} bpm'

    @classmethod
    def from_input(cls):
        return cls(
            rf.InputFunction('Resting Pulse: ',1, rf.isInteger),
            rf.InputFunction('Age: ',1, rf.isInteger)
        )

    def targetHeartRate(self, intensity):
        return round((220-self.age-self.restingPulse)*intensity/100 + self.restingPulse)

    def show(self):
        fig, ax = plt.subplots()

        # hide axes
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')

        column = ['Intensity','Rate']
        df = pd.DataFrame(self.data, columns=column)
        ax.table(cellText=df.values, colLabels=df.columns, loc='center')
        fig.tight_layout()
        plt.show()

    def show01(self):
        print('Intensity  | Rate')
        print('-----------|------')
        for row in self.data:
            print(f'{row[0]}        | {row[1]}')

mainFunction = InputData.from_input()
mainFunction.show01()