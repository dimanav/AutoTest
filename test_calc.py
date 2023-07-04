import ctypes
import unittest

name = 'C:\\Users\\user\\source\\repos\\Calc\\x64\\Release\\Calc.dll'

library = ctypes.CDLL(name)

class CalcTest(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(library.add(5, 3), 8)
        self.assertEqual(library.add(-2, 1), -1)
        self.assertEqual(library.add(-5, -3), -8)
        self.assertEqual(library.add(1, -2), -1)

    def test_sub(self):
        self.assertEqual(library.subtract(5, 3), 2)
        self.assertEqual(library.subtract(-2, 1), -3)
        self.assertEqual(library.subtract(-5, -3), -2)
        self.assertEqual(library.subtract(1, -2), 3)

    def test_mul(self):
        self.assertEqual(library.multiply(5, 3), 15)
        self.assertEqual(library.multiply(-2, 1), -2)
        self.assertEqual(library.multiply(-5, -3), 15)
        self.assertEqual(library.multiply(1, -2), -2)



if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(stream=open('test_results.txt', 'w')))
    