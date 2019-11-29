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

    def test_death(self):
        x,y = 2,0
        value = 3
        self.world.set(x,y,value)
        
        if (8 - self.world.get_neighbours(x,y).count(0)) == 0:
            self.world.set(x,y,0)        
    
        get_value = self.world.get(x,y)
        self.assertEqual(get_value,0)


    def test_less_then_two_neighbours(self):
        x,y = 2,2
        value = 3
        self.world.set(x,y,value)
        self.world.set(x,y-1,value)
        
        
        if (8 - self.world.get_neighbours(x,y).count(0)) < 2:
            self.world.set(x,y,0)        
    
        get_value = self.world.get(x,y)
        self.assertEqual(get_value,0)  
   




    
if __name__ == '__main__':
    unittest.main()