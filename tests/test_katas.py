import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        """Test if add() adds x and y."""
        self.assertEqual(katas.add(5, 2), 7)

    def test_multiply(self):
        """Test if multiply() multiplies x by y."""
        self.assertEqual(katas.multiply(5, 2), 10)

    def test_power(self):
        """Test if power() returns the result of taking x to the nth power."""
        self.assertEqual(katas.power(5, 2), 25)

    def test_factorial(self):
        """Test if factorial() returns result of calculating the factorial of n."""
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        """Test if fibonacci() returns the nth number in the fibonacci sequence (starting at 0)."""
        self.assertEqual(katas.fibonacci(5), 3)


if __name__ == '__main__':
    unittest.main()
