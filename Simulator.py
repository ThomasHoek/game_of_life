from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, BSA = "B3/S23/A1"):
        """
        Constructor for Game of Life simulator.

        :param world: (optional) environment used to simulate Game of Life.
        """
        self.generation = 0

        
        try:
            self.birth, self.survival,self.age = BSA.split("/")
        except:
            print("error in birth, survival and age input")
            self.birth = "B3"
            self.survival = "S23"
            self.age = "A1"
            
        if world == None:
            self.world = World(20)
        else:
            self.world = world


    
    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1


        birth = self.birth[1:]
        survival = self.survival[1:]
        age = self.age[1:]

        coordinatelist = []
        for y in range(self.world.height):
            coordinatelist.append([])
            for x in range(self.world.width):

                neighbour_list = self.world.get_neighbours(x, y)
                count_zeros = (8 - neighbour_list.count(0))

                curr_value = self.world.get(x, y)

                if curr_value and (str(count_zeros) not in survival):
                    coordinatelist[y].append(curr_value - 1)

                # With list comprehention it checks the amount of numbers that are between age min+2 and max+2
                # if that number is in birth it accepts.
                else:
                    total_fertile = str(sum([1 if (x > 2 and x < (int(age)-2)) else 0 for x in neighbour_list]))
                    if (total_fertile in birth) or (age == "1" and str(count_zeros) in birth):
                        coordinatelist[y].append(age)

                    else:
                        coordinatelist[y].append(curr_value)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x, y, coordinatelist[y][x])


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