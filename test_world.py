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
        input_BS = "B1/S1"
        self.birth , self.survival = input_BS.split("/")

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
        else:
            self.world.set(x,y,value)
    
        get_value = self.world.get(x,y)
        self.assertEqual(get_value,0)  
   

    def test_die_more_then_three(self):
        x,y = 2,2
        value = 3
        self.world.set(x,y,value)
        self.world.set(x,y-1,value)
        self.world.set(x,y+1,value)
        self.world.set(x-1,y,value)
        self.world.set(x+1,y,value)
        
        count_zeros = (8 - self.world.get_neighbours(x,y).count(0))
        if (count_zeros < 2) or (count_zeros > 3):
            self.world.set(x,y,0)        
        else:
            self.world.set(x,y,value)

        get_value = self.world.get(x,y)
        self.assertEqual(get_value,0)  


    def test_survival(self):
        x,y = 2,2
        value = 3
        self.world.set(x,y,value)
        self.world.set(x,y-1,value)
        self.world.set(x,y+1,value)
        self.world.set(x-1,y,value)
        
        
        count_zeros = (8 - self.world.get_neighbours(x,y).count(0))
        if (count_zeros < 2) or (count_zeros > 3):
            self.world.set(x,y,0)
        else:
            self.world.set(x,y,value)

        get_value = self.world.get(x,y)
        self.assertEqual(get_value,value)  
    

    def test_birth(self):
        x,y = 2,2
        value = 0
        self.world.set(x,y-1,value)
        self.world.set(x,y+1,value)
        self.world.set(x-1,y,value)
        
        
        count_zeros = (8 - self.world.get_neighbours(x,y).count(0))
        if value and ((count_zeros < 2) or (count_zeros > 3)):
            self.world.set(x,y,0)
        elif ((count_zeros >= 2) or (count_zeros < 4)):
            self.world.set(x,y,1)
        else:
            self.world.set(x,y,value)

        get_value = self.world.get(x,y)
        self.assertEqual(get_value,1)  


    def test_entire_grid(self):
        x1,y1 = 2,5
        x2,y2 = 3,5
        x3,y3 = 4,5

        #  ---     -> should return |

        value = 1
        self.world.set(x1,y1,value)
        self.world.set(x2,y2,value)
        self.world.set(x3,y3,value)
        
        coordinatelist = []
        for y in range(self.world.height):
            coordinatelist.append([])
            for x in range(self.world.width):
                count_zeros = (8 - self.world.get_neighbours(x,y).count(0))
                if value and ((count_zeros < 2) or (count_zeros > 3)):
                    coordinatelist[y].append(0)

                elif ((count_zeros >= 2) or (count_zeros < 4)):
                    coordinatelist[y].append(1)

                else:
                    coordinatelist[y].append(value)


        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x,y,coordinatelist[y][x])



        get_value_old1 = self.world.get(x1,y1)
        get_value_old2 = self.world.get(x2,y2)
        get_value_old3 = self.world.get(x3,y3)

        self.assertEqual(get_value_old1,0)  
        self.assertEqual(get_value_old2,1)  
        self.assertEqual(get_value_old3,0)  


        get_value_new1 = self.world.get(x1,y1+1)
        get_value_new2 = self.world.get(x1,y1-1)        
        self.assertEqual(get_value_new1,1)  
        self.assertEqual(get_value_new2,1)  
    

    def test_input_birth(self):
        
        x1,y1 = 5,5
        birth = "B1"
        birth = self.birth[1:]


        value = 1
        self.world.set(x1,y1,value)

        
        coordinatelist = []
        for y in range(self.world.height):
            coordinatelist.append([])
            for x in range(self.world.width):
                count_zeros = (8 - self.world.get_neighbours(x,y).count(0))

                if value and (str(count_zeros) not in birth):
                    coordinatelist[y].append(0)

                elif str(count_zeros) in birth:
                    coordinatelist[y].append(1)

                else:
                    coordinatelist[y].append(value)


        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x,y,coordinatelist[y][x])



        var_get_neighbours = self.world.get_neighbours(x1,y1).count(0)
        self.assertEqual(var_get_neighbours,0)  
        
        var_get_birth = self.world.get(x1,y1)
        self.assertEqual(var_get_birth,0)  
        

if __name__ == '__main__':
    unittest.main()
