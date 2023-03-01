# here we will test the Point class

import unittest # built in to Python
from my_points import Point # this is the class we will test

# test driven development
# 0 - have a 'spec
# 1 - write a test
# 2 - write code
# 3 - stop writing code when it passes tests


# when writing tests we inherit from 'TestCase'
class testPoint(unittest.TestCase):
    # set up before each test
    def setUp(self):
        self.p = Point(3,5) # runs BEFORE every test
    # NB we need to ensure tests do NOT rely on other tests
    def testMoveByXY(self):
        '''Test we can move by x and y values'''
        self.p.moveBy(5, 2)
        expected = self.p.display() # a tuple of where the point is now
        # make an assertion < > == <= >= !=
        self.assertEqual( expected, (8, 7) )
    def testMoveByNegXY(self):
        '''Test we can move by -ve x and y values'''
        self.p.moveBy(-5, -2)
        expected = self.p.display() # a tuple of where the point is now
        # make an assertion
        self.assertEqual( expected, (-2, 3) )
    def testMoveByX(self):
        '''if we leave y blank, it should use default zero'''
        self.p.moveBy(dx=9) # only x not y
        self.assertEqual(self.p.display(), (12, 5))
    def testHypot(self):
        '''Derive the hypotenuse from x and y'''
        self.p.moveBy(0,-1) # leaves us at (3,4)
        r = self.p.hypot()
        self.assertAlmostEqual(r, 5.00, places=2)
    def testPosi_neg_hypot_equal(self):
        '''the hypot for +ve x and y should equal that of -ve x and y'''
        self.pos_h = Point(3,4)
        self.neg_h = Point(-3, -4)
        self.assertAlmostEqual( self.pos_h.hypot(), self.neg_h.hypot(), places=2 )
    def testStringValueFails(self):
        '''if x or y ar entered as strings, we should raise an exception'''
        with self.assertRaises(TypeError):
            Point('3', 4)

if __name__ == '__main__':
    unittest.main()  #invoke the tests