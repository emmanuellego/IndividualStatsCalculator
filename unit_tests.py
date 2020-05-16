import unittest
import random
from calculator import Calculator
from rand_gen import RandomGenerator
from desc_stats import DescStats
from pop_sampling import PopSampling


class TestOperations(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5, "Must be 5")

    def test_subtr(self):
        self.assertEqual(Calculator.subtr(3, 2), 1, "Must be 1")

    def test_multi(self):
        self.assertEqual(Calculator.multi(2, 3), 6, "Must be 6")

    def test_divide(self):
        self.assertEqual(Calculator.divide(4, 2), 2, "Must be 2")

    def test_root(self):
        self.assertEqual(Calculator.root(25), 5, "Must be 5")

    def test_square(self):
        self.assertEqual(Calculator.square(2), 4, "Must be 4")

    def test_nthroot(self):
        self.assertEqual(Calculator.nthroot(3, 27), 3, "Must be 3")

    def test_power(self):
        self.assertEqual(Calculator.power(2, 3), 8, "Must be 8")

    def test_addsums(self):
        r = [1, 2, 3]
        self.assertEqual(Calculator.addsums(r), 6, "Must be 6")


class TestRandoms(unittest.TestCase):

    def test_random(self):
        random.seed(1)
        r = random.randrange(0, 5)
        self.assertEqual(RandomGenerator.random_seed(0, 5, 1), r)

    def test_random_list(self):
        random.seed(2)
        rlist = []
        for i in range(0, 5):
            x = random.randrange(0, 5)
            rlist.append(x)
        self.assertEqual(RandomGenerator.random_list_seed(0, 5, 5, 2), rlist)

    def test_random_item(self):
        random.seed(3)
        r = random.choice([1, 2, 3])
        self.assertEqual(RandomGenerator.random_item_seed([1, 2, 3], 3), r)

if __name__ == '__main__':
    unittest.main()
