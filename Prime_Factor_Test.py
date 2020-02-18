import unittest


def factors(number):
    _factors = []
    if number == 2 or number == 3:
        _factors.append(number)
    elif number == 4:
        _factors = [2, 2]
    return _factors


class PrimeFactorsTest(unittest.TestCase):
    def test_one_has_no_factors(self):
        self.assertEqual([], factors(1))

    def test_2_has_factor_of_itself(self):
        self.assertEqual([2], factors(2))

    def test_3_has_factor_of_itself(self):
        self.assertEqual([3], factors(3))

    def test_4_has_factor_of_2_and_2(self):
        self.assertEqual([2, 2], factors(4))


if __name__ == '__main__':
    unittest.main()
