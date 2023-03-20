import numpy as np
import re
from Capacitor import Capacitor

def displayDielectrics():
    dielectric_constants = {1: "Air, εᵣ = 1", 2: "Teflon, εᵣ = 2.1", 3: "Polyethylene, εᵣ = 2.25",
                            4: "Polyimide, εᵣ = 3.4"}
    print("\nAvailable Dielectrics:")
    for i in range(len(dielectric_constants)):
        print("({}) {}".format(i + 1, dielectric_constants[i + 1]))

def inputScript():
    values = []
    relative_permitivity = {1: 1, 2: 2.1, 3: 2.25, 4: 3.4}
    userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(cm), and the distance "
                "between the plates(mm):\n")
    data = re.split('[,/ "\-;:\\\]+', userInput, 3)
    values = [float(s) for s in data if s.isdigit()]
    while(len(values) != 3):
        if (len(values)<3):
            print("Invalid input. Only enter numbers separated by some delimiter.")
            userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(cm), and the "
                              "distance between the plates(mm):\n")
            data = re.split('[,/ _"\-;:\\\]+', userInput, 3)
            values = [s for s in data if s.isdigit()]
        else:
            print("Too many inputs. Only enter numbers corresponding to the dielectric, area, and separation_distance.")
            userInput = input("Select your dielectric(number), choose the area of the capacitor's plates(cm), and the "
                              "distance between the plates(mm):\n")
            data = re.split('[,/ _"\-;:\\\]+', userInput, 3)
            values = [s for s in data if s.isdigit()]

    dielectric = relative_permitivity[int(values[0])]
    area = values[1]
    distance = values[2]
    return [dielectric, area, distance]

displayDielectrics()
parameters = inputScript()
cap1 = Capacitor(parameters[0], parameters[1], parameters[2])
cap1.capacitance()
cap1.breakdownVoltage()