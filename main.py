from Visualisation import *
from Simulator import *
import time

# Configuratie
VISUALISATION=True

if __name__ == "__main__":
    w = World(25)
    
    BSA = input("What is de birth and survival and age\n")
    sim = Simulator(w,BSA)
    
    
    if VISUALISATION:
        vis = Visualisation(sim)
    else:
        while True:
            # Create new world and print to screen
            print(sim.update())
            # slow down simulation
            time.sleep(0.5)