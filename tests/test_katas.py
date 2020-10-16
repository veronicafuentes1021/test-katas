import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(2, 4), 6)
        self.assertEqual(katas.add(5, -7), -2)
        self.assertEqual(katas.add(-9, -3), -12)
        self.assertEqual(katas.add(1.26, 6.46), 7.72)

    def test_multiply(self):
        self.assertEqual(katas.multiply(1, 4), 4)
        self.assertEqual(katas.multiply(2, 4), 8)
        self.assertEqual(katas.multiply(5, -7), -35)
        self.assertEqual(katas.multiply(-9, -3), 27)

    def test_power(self):
        self.assertEqual(katas.power(2, 4), 16)
        self.assertEqual(katas.power(5, 7), 78125)
        self.assertEqual(katas.power(-9, 3), -729)

    def test_factorial(self):
        self.assertEqual(katas.factorial(2), 2)
        self.assertEqual(katas.factorial(5), 120)
        self.assertEqual(katas.factorial(9), 362880)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(2), 1)
        self.assertEqual(katas.fibonacci(7), 13)
        self.assertEqual(katas.fibonacci(3), 2)
        self.assertEqual(katas.fibonacci(6), 8)


if __name__ == '__main__':
    unittest.main()
