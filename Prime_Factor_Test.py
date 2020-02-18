import unittest

def factors(number):
    if number == 2:
        return [2]
    return []

class PrimeFactorsTest(unittest.TestCase):
    def test_one_has_no_factors(self):
        self.assertEqual([], factors(1))

    def test_2_has_factor_of_itself(self):
        self.assertEqual([2],factors(2))

if __name__ == '__main__':
    unittest.main()