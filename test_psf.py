import unittest
import numpy as np
import point_sets_fitting as psf


class PsfTester(unittest.TestCase):

    def test_center(self):

        testInput = np.mat('0  0  0; 0  4  0 ; 8  0  0; 0  0  12').transpose()
        centerIs = np.mat('2; 1; 3')
        centerComputed = psf.getPointSetCenter(testInput)
        self.assertTrue(np.array_equal(centerIs,centerComputed))


if __name__ == '__main__':
    unittest.main()