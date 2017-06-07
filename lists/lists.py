#!/usr/bin/python

'''
    create new list squares, loop range and append
'''
squares = []

for i in range(10):
    squares.append(i**2)

print squares

'''
    using list comprehension
'''

com_squares = [s**2 for s in range(10)]
print com_squares

ln = len(com_squares)
print ln

'''
    assign com_squares to cs, not a copy
    actions on cs, also on com_squares

'''
cs = com_squares

cs.remove(0)

print cs, com_squares

com_squares.insert(0, 0)

print cs, com_squares

com_squares.reverse()

print cs, com_squares
