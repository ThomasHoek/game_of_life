import unittest
from World import *


class TestWorld(unittest.TestCase):
    """
    Test cases for ``World`` data type.
    """
    def setUp(self):
        """
        Common setup for running tests
        """
        self.width, self.height = 10, 12
        self.world = World(self.width, self.height)

    def test_set(self):
        """
        Tests setting value on location (x,y).
        """
        x, y = 4, 6
        self.world.set(x, y)
        self.assertEqual(self.world.world[y][x], 1)
        value = 7
        self.world.set(x, y, 7)
        self.assertEqual(self.world.world[y][x], 7)

    def test_get(self):
        """
        Tests getting value from location (x, y).
        """
        x, y = 3, 5
        value = 3
        self.world.world[y][x] = 3
        self.assertEqual(self.world.get(x, y), value)

    def test_get_neighbours(self):
        """
        Tests getting neighbours from location.
        """
        x, y = 2, 0
        value = 4
        self.world.set(x, self.height-1, value)
        neighbours = self.world.get_neighbours(x, y)
        self.assertEqual(8, len(neighbours))
        self.assertIn(value, neighbours)


    def test_try_death(self):
        x, y = 2 , 0
        value = self.world.get(x,y)
        self.world.set(x,y,0)


    def test_neighbours_then_death(self):
        x, y = 2 , 0
        value = self.world.get(x,y)
        zeros = self.world.get_neighbours(x,y).count(0)
        if (8-zeros) == 2 or  (8-zeros) == 3:
            self.world.set(x,y,1)
        else:
            self.world.set(x,y,0)

    def test_allgrid(self):
        x,y = 0,0
        self.world.set(x,y,1)
        listgrid = []
        for y in range(self.world.height):
            listgrid.append([])
            for x in range(self.world.width):
                value = self.world.get(x,y)
                zeros = self.world.get_neighbours(x,y).count(0)
                
                if (8 - zeros) == 2 or (8-zeros) == 3:
                    listgrid[y].append(1)
                else:
                    listgrid[y].append(0)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x,y, listgrid[y][x])

    def test_add_cells(self):
        x,y = 0,0
        self.world.set(x,y,1)

        listgrid = []
        for y in range(self.world.height):
            listgrid.append([])
            for x in range(self.world.width):
                value = self.world.get(x,y)
                zeros = self.world.get_neighbours(x,y).count(0)
                
                if value and ((8 - zeros) == 2 or (8-zeros) == 3):
                    listgrid[y].append(value)
                elif (8-zeros) == 3:
                    listgrid[y].append(1)
                else:
                    listgrid[y].append(0)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x,y, listgrid[y][x])  
        

    def test_different_amount_neighbours(self):
        x,y = 0,0
        self.world.set(x,y,1)
        zeros = self.world.get_neighbours(x,y).count(0)
        
        inputmain = "B358/S237"

        birth , survival = inputmain.split("/")
        birth = birth[1:]
        survival = survival[1:]
        

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


    def test_age(self):
        x,y = 0,0
        self.world.set(x,y,1)
        zeros = self.world.get_neighbours(x,y).count(0)
        
        inputmain = "B358/S237"

        birth , survival = inputmain.split("/")
        birth = birth[1:]
        survival = survival[1:]
        
        listgrid = []




        for y in range(self.world.height):
            listgrid.append([])
            for x in range(self.world.width):

                number_fertile = str(sum(1 if ((x > 2) and (x < (self.age - 2))) else 0 for x in self.world.get_neighbours(x,y)))
                value = self.world.get(x,y)
                zeros = self.world.get_neighbours(x,y).count(0)
                
                if value and str(8 - zeros) in survival:    
                    # survival behoud
                    listgrid[y].append(value)

                
                elif number_fertile in birth:
                # elif str(8-zeros) in birth:
                    listgrid[y].append(self.age)

                elif (value == 0):
                    listgrid[y].append(0)

                else:
                    listgrid[y].append(value-1)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x,y, listgrid[y][x])  




    
if __name__ == '__main__':
    unittest.main()