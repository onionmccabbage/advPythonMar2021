# testing the Point class
import unittest
from my_points import Point

class testPoint(unittest.TestCase): # we name tests like this

    # we can set up before each test
    def setUp(self):
        # this method will be called before each test
        self.point = Point(3, 5)

    # declare a test
    def testMoveBy1(self):
        '''testing the moveBy method'''
        self.point.move_by(5, 2)
        # make an assertion
        self.assertEqual(self.point.display(), (8, 7))
        
    def testMoveBy2(self):
        '''testing the moveBy method'''
        self.point.move_by(-5, -2)
        # make an assertion
        self.assertEqual(self.point.display(), (-2, 3))



if __name__ == '__main__':
    # unittest will look for any classses whose name begins with 'test'
    unittest.main() # this will run all tests