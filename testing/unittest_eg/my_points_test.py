# testing the Point class
import unittest
from my_points import Point

class testPoint(unittest.TestCase): # we name tests like this

    # we can set up before each test
    def setUp(self):
        # this method will be called before each test
        self.point = Point(3, 5)

    # declare tests
    def testPointCounter(self):
        self.assertGreater(Point.points, 0)
        # self.assertEqual(Point.points, 1) # fails

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

    def testHypot(self):
        ''' testing the hypotenuse is correctly returned'''
        self.point.move_by(0,-1) # now at (3,4)
        r = self.point.hypot()
        self.assertAlmostEqual(r, 5.00, places=2)
    
    def pos_neg_hypot_equal(self):
        self.p_positive = Point(3,4)
        self.p_negative = Point(-3,-4)
        self.assertAlmostEqual(self.p_negative.hypot(), self.p_positive.hypot(), places=2)

    def testStringValueFails(self):
        with self.assertRaises(TypeError):
            Point('3', 4)

if __name__ == '__main__':
    # unittest will look for any classses whose name begins with 'test'
    unittest.main() # this will run all tests