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
        age = 6
        self.age = age
        self.birth, self.survival = input_BS.split("/")

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
        '''
        Tests if a cell dies with no neighbours
        '''

        x, y = 2, 0
        value = 3
        self.world.set(x, y, value)

        # count the amount of zero's in the list.
        if (8 - self.world.get_neighbours(x, y).count(0)) == 0:
            self.world.set(x, y, 0)

        get_value = self.world.get(x, y)
        self.assertEqual(get_value, 0)

    def test_less_then_two_neighbours(self):
        '''
        Test for death if less then two neighbours
        '''
        x, y = 2, 2
        value = 3
        self.world.set(x, y, value)
        self.world.set(x, y-1, value)

        if (8 - self.world.get_neighbours(x, y).count(0)) < 2:
            self.world.set(x, y, 0)
        else:
            self.world.set(x, y, value)

        get_value = self.world.get(x, y)
        self.assertEqual(get_value, 0)

    def test_die_more_then_three(self):
        '''
        Tests if cell die if more then three neighbours
        '''
        x, y = 2, 2
        value = 3
        self.world.set(x, y, value)
        self.world.set(x, y-1, value)
        self.world.set(x, y+1, value)
        self.world.set(x-1, y, value)
        self.world.set(x+1, y, value)

        count_zeros = (8 - self.world.get_neighbours(x, y).count(0))
        if (count_zeros < 2) or (count_zeros > 3):
            self.world.set(x, y, 0)
        else:
            self.world.set(x, y, value)

        get_value = self.world.get(x, y)
        self.assertEqual(get_value, 0)

    def test_survival(self):
        '''
        Test if a cell survives if it has 3 neighbours
        '''
        x, y = 2, 2
        value = 3
        self.world.set(x, y, value)
        self.world.set(x, y-1, value)
        self.world.set(x, y+1, value)
        self.world.set(x-1, y, value)

        count_zeros = (8 - self.world.get_neighbours(x, y).count(0))

        # if amount of zeros in the code is less then two, or more then 3 then death.
        if (count_zeros < 2) or (count_zeros > 3):
            self.world.set(x, y, 0)
        else:
            self.world.set(x, y, value)

        get_value = self.world.get(x, y)
        self.assertEqual(get_value, value)

    def test_birth(self):
        '''
        Test if a cell gives birth to a new cell.
        '''

        x, y = 2, 2
        value = 0
        self.world.set(x, y-1, value)
        self.world.set(x, y+1, value)
        self.world.set(x-1, y, value)

        count_zeros = (8 - self.world.get_neighbours(x, y).count(0))
        # if a cell is alive (value) check if it survives
        if value and ((count_zeros < 2) or (count_zeros > 3)):
            self.world.set(x, y, 0)

        # if te amount of zeros are more then two or less then 4. Add a cell.
        elif ((count_zeros >= 2) or (count_zeros < 4)):
            self.world.set(x, y, 1)
        else:
            self.world.set(x, y, value)

        get_value = self.world.get(x, y)
        self.assertEqual(get_value, 1)

    def test_entire_grid(self):
        '''
        Tests if the entire world will be looped.
        '''
        x1, y1 = 2, 5
        x2, y2 = 3, 5
        x3, y3 = 4, 5

        #  ---     -> should return |

        value = 1
        self.world.set(x1, y1, value)
        self.world.set(x2, y2, value)
        self.world.set(x3, y3, value)

        coordinatelist = []
        # go throught he height of the world first
        for y in range(self.world.height):
            coordinatelist.append([])

            # Then though the width. Every Row is a list in which the values of the coordinates are.
            for x in range(self.world.width):
                count_zeros = (8 - self.world.get_neighbours(x, y).count(0))
                curr_value = self.world.get(x, y)
                if curr_value and ((count_zeros < 2) or (count_zeros > 3)):
                    coordinatelist[y].append(0)

                elif ((count_zeros >= 2) or (count_zeros < 4)):
                    coordinatelist[y].append(1)

                else:
                    coordinatelist[y].append(value)

        # which in the end get set.
        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x, y, coordinatelist[y][x])

        get_value_old1 = self.world.get(x1, y1)
        get_value_old2 = self.world.get(x2, y2)
        get_value_old3 = self.world.get(x3, y3)

        self.assertEqual(get_value_old1, 0)
        self.assertEqual(get_value_old2, 1)
        self.assertEqual(get_value_old3, 0)

        get_value_new1 = self.world.get(x1, y1+1)
        get_value_new2 = self.world.get(x1, y1-1)
        self.assertEqual(get_value_new1, 1)
        self.assertEqual(get_value_new2, 1)

    def test_input_birth(self):

        x1, y1 = 5, 5

        birth = self.birth[1:]
        # add a self birth

        value = 1
        self.world.set(x1, y1, value)

        coordinatelist = []
        for y in range(self.world.height):
            coordinatelist.append([])
            for x in range(self.world.width):
                count_zeros = (8 - self.world.get_neighbours(x, y).count(0))
                curr_value = self.world.get(x, y)

                if curr_value and ((count_zeros < 2) or (count_zeros > 3)):
                    coordinatelist[y].append(0)

                # checks if the amount of neighbours is in births.
                elif str(count_zeros) in birth:
                    coordinatelist[y].append(1)

                else:
                    coordinatelist[y].append(value)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x, y, coordinatelist[y][x])

        var_get_neighbours = self.world.get_neighbours(x1, y1).count(0)
        self.assertEqual(var_get_neighbours, 0)

        var_get_birth = self.world.get(x1, y1)
        self.assertEqual(var_get_birth, 0)

    def test_input_survival(self):

        x1, y1 = 5, 5
        x2, y2 = 5, 6

        birth = self.birth[1:]
        survival = self.survival[1:]

        value = 1
        self.world.set(x1, y1, value)
        self.world.set(x2, y2, value)

        coordinatelist = []
        for y in range(self.world.height):
            coordinatelist.append([])
            for x in range(self.world.width):
                count_zeros = (8 - self.world.get_neighbours(x, y).count(0))
                curr_value = self.world.get(x, y)
                # checks if the cell is alive and the amount of neighbours are in survival.
                if curr_value and (str(count_zeros) not in survival):
                    coordinatelist[y].append(0)

                elif str(count_zeros) in birth:
                    coordinatelist[y].append(1)

                else:
                    coordinatelist[y].append(value)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x, y, coordinatelist[y][x])

        var_get_survival1 = self.world.get(x1, y1)
        self.assertEqual(var_get_survival1, 1)

        var_get_survival2 = self.world.get(x2, y2)
        self.assertEqual(var_get_survival2, 1)

    def test_decay(self):

        x1, y1 = 5, 5
        x2, y2 = 2, 2

        birth = self.birth[1:]
        survival = self.survival[1:]

        value = 6
        value2 = 1

        self.world.set(x1, y1, value)
        self.world.set(x2, y2, value2)

        coordinatelist = []
        for y in range(self.world.height):
            coordinatelist.append([])
            for x in range(self.world.width):
                count_zeros = (8 - self.world.get_neighbours(x, y).count(0))

                curr_value = self.world.get(x, y)
                if value and (str(count_zeros) not in survival):
                    coordinatelist[y].append(curr_value - 1)
                    # a cells current age will be lowered by one

                elif str(count_zeros) in birth:
                    coordinatelist[y].append(1)

                else:
                    coordinatelist[y].append(curr_value)
                    # else it stays the same age.

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x, y, coordinatelist[y][x])

        var_get_decay = self.world.get(x1, y1)
        self.assertEqual(var_get_decay, 5)

        var_get_decay2 = self.world.get(x2, y2)
        self.assertEqual(var_get_decay2, 0)

    def test_survival_birth(self):

        x1, y1 = 5, 5
        x2, y2 = 2, 2

        birth = self.birth[1:]
        survival = self.survival[1:]
        age = self.age

        value = 6
        value2 = 3

        self.world.set(x1, y1, value)
        self.world.set(x2, y2, value2)

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
                    total_fertile = str(
                        sum([1 if (x > 2 and x < (age-2)) else 0 for x in neighbour_list]))
                    if (total_fertile in birth):
                        coordinatelist[y].append(age)

                    else:
                        coordinatelist[y].append(curr_value)

        for y in range(self.world.height):
            for x in range(self.world.width):
                self.world.set(x, y, coordinatelist[y][x])

        var_get_birth = self.world.get_neighbours(x1, y1).count(0)
        self.assertEqual(var_get_birth, 8)

        var_get_survival = self.world.get(x1, x2)
        self.assertEqual(var_get_survival, 0)

        var_get_birth2 = self.world.get_neighbours(x2, y2).count(0)
        self.assertEqual(var_get_birth2, 0)


        


if __name__ == '__main__':
    unittest.main()
