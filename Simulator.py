from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world

    def update(self, inputmain = "B3/S23") -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        try:
            birth , survival = inputmain.split("/")
            birth = birth[1:]
            survival = survival[1:]
        except:
            birth = "3"
            survival = "23"


        listgrid = []
        for y in range(self.world.height):
            listgrid.append([])
            for x in range(self.world.width):
                value = self.world.get(x,y)
                zeros = self.world.get_neighbours(x,y).count(0)
                
                if value and str(8 - zeros) in survival:
                    listgrid[y].append(value)
                elif str(8-zeros) in birth:
                    listgrid[y].append(1)
                else:
                    listgrid[y].append(0)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x,y, listgrid[y][x])  

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world