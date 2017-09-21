#!/usr/bin/python

import unittest


''' funcs to test'''
def square(val):
    return val * val

def whatAmI(val):
    return val


class MyFirstTest(unittest.TestCase):
    ''' test func sq pass'''
    def testPass(self):
        self.assertEqual(square(2),4)
    ''' test func sq fail'''
    def testFail(self):
        self.assertEqual(square(3),10)
    ''' test param is alpha'''
    def testValString(self):
        self.assertTrue(whatAmI('iamstring').isalpha())
    ''' test param digit''' 
    def testValNum(self):
        self.assertTrue(whatAmI('2').isdigit())



if __name__ == '__main__':
    unittest.main()