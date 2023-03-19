import numpy as np
import matplotlib as plt

class Capacitor:
    def __init__(self, permitivity, area, distance):
        self.permitivity = permitivity
        self.area = area
        self.distance = distance

    def capacitance(self):
        self.capacitance = self.permitivity*8.854*10**-12*self.area*10**13/(self.distance)
        print("C = {} pF".format(self.capacitance))

    def breakdownVoltage(self):
        self.bdv = self.permitivity * self.distance
        print("V_BR = {} Volts".format(self.bdv))
