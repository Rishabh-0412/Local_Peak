import unittest


def get_peak(value):
    return value


class LocalPeakTest(unittest.TestCase):
    def test_peak_when_array_has_one_element(self):
        self.assertEqual(2, get_peak(2))