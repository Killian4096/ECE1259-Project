import numpy as np
import keyboard
import time
import sys
import re
from Capacitor import Capacitor

dielectric_constants = {1: "Air, εᵣ = 1", 2: "Teflon, εᵣ = 2.1", 3: "Polyethylene, εᵣ = 2.25",
                          4: "Polyimide, εᵣ = 3.4"}
relative_permitivity = {1: 1, 2: 2.1, 3: 2.25, 4: 3.4}
print("\nAvailable Dielectrics:")
for i in range(len(dielectric_constants)):
    print("({}) {}".format(i+1, dielectric_constants[i+1]))
choice, area, distance = input("Select your dielectric(number) and choose the area of the capacitor's plates(cm), and the distance between "
                               "the plates(mm):\n").split(' ', 3)
cap1 = Capacitor(relative_permitivity[int(choice)], float(area), float(distance))
cap1.capacitance()
cap1.breakdownVoltage()