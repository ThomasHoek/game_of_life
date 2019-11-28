from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(50)
    sim = Simulator(w)
    inputmain = input("What birth and survival?")
    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update(inputmain))
            # slow down simulation
            time.sleep(0.5)