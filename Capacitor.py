import numpy as np
import matplotlib as plt

class Capacitor:
    def _init_(self):
        self.separationDistance = 0
        self.area = 0
        self.chargeDensity = 0
        self.charge = 0
        self.temperature = 0
        self.capacitance = 0
        self.resistance = 0
        self.voltage = 0
        self.current = 0
        self.breakdownVoltage = 0
        self.dielectricStrength = 0
        self.conductivity = 0
        self.leakageCurrent = 0
        self.electricField = 0
        self.frequency = 0
        self.materials = {1: "Air, εᵣ = 1", 2: "Teflon, εᵣ = 2.1", 3: "Polyethylene, εᵣ = 2.25"}
        self.power = 0
        self.capacitorType = 0
        self.epsilonNaught = 8.854*10**-12
        print("Choose the dielectric you want to use for your capacitor: \n")
        #print("(1) Air, εᵣ = 1\n(2)Teflon, εᵣ = 2.1\n(3) Polyethylene, εᵣ")
