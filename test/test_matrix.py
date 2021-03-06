""" Matrix module unit tests. """
# pylint: disable=C0111,R0904,C0326,C0103,W0142
from .. import matrix
import unittest


class TestMatrixFunctions(unittest.TestCase):

    def setUp(self):
        self.matrix = matrix.Matrix()

    def tearDown(self):
        self.matrix = None

    def test_zero(self):
        self.matrix = matrix.Matrix.zero(4, 3)
        zero_array = [[0 for _ in range(3)] for _ in range(4)]
        self.assertEqual(self.matrix.value, zero_array)
        self.assertRaises(ValueError, self.matrix.zero, *(-1, 3))
        self.assertRaises(ValueError, self.matrix.zero, *(2, 0))
        self.assertRaises(ValueError, self.matrix.zero, *(-1, -1))

    def test_identity(self):
        self.matrix = matrix.Matrix.identity(5)
        func = lambda x, y: 1 if x == y else 0
        ident_array = [[func(i, j) for i in range(5)] for j in range(5)]
        self.assertEqual(self.matrix.value, ident_array)
        self.assertRaises(ValueError, self.matrix.identity, *(-1,))

    def test_indexing(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        self.matrix = matrix.Matrix(array)
        for x in range(3):
            for y in range(3):
                self.assertEqual(self.matrix[x][y], array[x][y])

    def test_size(self):
        array = [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9],
                 [1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]]
        self.matrix = matrix.Matrix(array)
        self.assertEqual(self.matrix.size(), (6, 3))

    def test_add(self):
        self.matrix = matrix.Matrix.zero(4, 3)
        other = matrix.Matrix.zero(4, 3)
        other2 = matrix.Matrix.zero(4, 4)
        new = self.matrix + other
        with self.assertRaises(ValueError):
            _ = self.matrix + other2
        self.assertEqual(self.matrix.value, new.value)

    def test_add2(self):
        self.matrix = matrix.Matrix.identity(3)
        other = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        new = self.matrix + other - other
        self.assertEqual(self.matrix.value, new.value)

    def test_property(self):
        self.matrix = matrix.Matrix.identity(3)
        new = matrix.Matrix()
        new.value = self.matrix.value
        self.assertEqual(new.size(), self.matrix.size())
        self.matrix.value = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(self.matrix.value, [[1, 2, 3], [4, 5, 6]])
        self.assertEqual(self.matrix.size(), (2, 3))

    def test_transpose(self):
        self.matrix = matrix.Matrix.identity(3)
        self.assertEqual(self.matrix, self.matrix.T)
        new = matrix.Matrix([[1, 2, 3], [4, 5, 6]])
        self.assertEqual(new.T.size(), (3, 2))
        self.assertEqual(new, new.T.T)

    def test_multiply(self):
        self.matrix = matrix.Matrix.identity(3)
        other = matrix.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(self.matrix * other, other)
        self.assertEqual(matrix.Matrix.zero(3, 3) * self.matrix,
                         matrix.Matrix.zero(3, 3))
        self.matrix = matrix.Matrix([[1, 1, 1], [2, 2, 2]])
        self.assertEqual((self.matrix * self.matrix.T).size(), (2, 2))
        self.assertEqual((self.matrix.T * self.matrix).size(), (3, 3))
        self.matrix = matrix.Matrix([[-1, 0], [0, 1]])
        self.assertEqual(self.matrix * self.matrix, matrix.Matrix.identity(2))

    def test_lu(self):
        self.matrix = matrix.Matrix()
        array = [[1, 0, 4], [2, 5, 0], [1, 5, 2]]
        self.matrix.value = array
        P, L, U = self.matrix.LU()
        self.assertEqual(P * self.matrix, L * U)
        self.matrix = matrix.Matrix.identity(10)
        P, L, U = self.matrix.LU()
        self.assertEqual(self.matrix, L)
        self.assertEqual(self.matrix, U)
        self.assertEqual(self.matrix, L * U)

if __name__ == "__main__":
    SUITE = unittest.TestLoader().loadTestsFromTestCase(TestMatrixFunctions)
    unittest.TextTestRunner(verbosity=2).run(SUITE)
