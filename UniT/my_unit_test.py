#!/usr/bin/python

import unittest


''' funcs to test'''
def square(val):
    return val * val

def whatAmI(val):
    return val


class MyFirstTest(unittest.TestCase):
    ''' test func sq pass'''
    def test_pass(self):
        self.assertEqual(square(2),4)
    ''' test func sq fail'''
    def test_fail(self):
        self.assertEqual(square(3),10)
    ''' test param is alpha'''
    def test_val_string(self):
        self.assertTrue(whatAmI('iamstring').isalpha())
    ''' test is upper'''
    def test_upper(self):
        self.assertTrue(whatAmI('HELLO').isupper())
    ''' test is ! upper'''
    def test_not_upper(self):
        self.assertTrue(whatAmI('hello').isupper())
    ''' test param digit''' 
    def test_val_num(self):
        self.assertTrue(whatAmI('2').isdigit())



if __name__ == '__main__':
    unittest.main()