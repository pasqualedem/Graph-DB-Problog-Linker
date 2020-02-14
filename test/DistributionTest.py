import unittest
from Distribution import Multinomial, Normal, Interspersed


class MyTestCase(unittest.TestCase):
    def test_multinomial(self):
        expected = {1: 0.16842105263157894, 2: 0.2, 3: 0.18947368421052632, 4: 0.17894736842105263,
                    5: 0.14736842105263157, 6: 0.11578947368421053}
        data = [1, 2, 1, 3, 4, 1, 4, 5, 3, 2, 2, 3, 5, 3, 3, 2, 1, 2, 4, 3, 2, 2, 1, 2, 3, 4, 4, 5, 5, 6, 4, 3, 1, 2, 4]
        pseudocounts = {1: 10, 2: 10, 3: 10, 4: 10, 5: 10, 6: 10}
        mult = Multinomial(pseudocounts)

        for num in data:
            mult.add(num)

        result = mult.get_parameters()
        self.assertAlmostEqual(expected, result)

    def test_interspersed(self):
        data = [12, 43, 41, 32, 34, 12, 43, 24, 21, 45, 34, 32, 10, 1, 2, 4, 49, 27, 11, 23]
        expected = {'[10, 20]': 0.15, '[40, 50]': 0.25, '[30, 40]': 0.2, '[20, 30]': 0.2, '[0, 10]': 0.2}
        intervals = [0, 10, 20, 30, 40, 50]
        inter = Interspersed(intervals)

        for num in data:
            inter.add(num)

        result = inter.get_parameters()
        print(result)
        self.assertAlmostEqual(expected, result)

    def test_continuous(self):
        data = [12, 43, 41, 32, 34, 12, 43, 24, 21, 45, 34, 32, 10, 1, 2, 4, 49, 27, 11, 23]
        normal = Normal()

        for num in data:
            normal.add(num)

        result = normal.get_parameters(recalculate=True)
        self.assertAlmostEqual(25, result[0])
        self.assertAlmostEqual(15.33829057929, result[1])


if __name__ == '__main__':
    unittest.main()
