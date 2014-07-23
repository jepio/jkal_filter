"""
A module implementing the Matrix class.
Based on:
https://github.com/ozzloy/udacity-cs373/blob/master/unit-2.py
"""

class Matrix(object):
    """ A matrix class covering all major matrix operations. """

    def __init__(self, value=None):
        """ Create a matrix from list of lists. """
        if value is None:
            value = [[]]
        self.value = value
        self.dimx = len(value)
        self.dimy = len(value[0])
        #if value == [[]]:
        #    self.dimx = 0

    def zero(self, dimx, dimy):
        """ Zero the matrix. """
        if dimx < 1 or dimy < 1:
            raise ValueError("Invalid size of matrix")
        else:
            self.dimx = dimx
            self.dimy = dimy
            self.value = [[0 for _ in range(dimy)] for _ in range(dimx)]

    def identity(self, dim):
        """ Make the matrix an identity. """
        self.zero(dim, dim)
        for i in range(dim):
            self.value[i][i] = 1

    def show(self):
        """ Print the matrix. """
        for i in range(self.dimx):
            print self.value[i]
        print ' '
