import unittest


def get_peak(num_list):
    return num_list


class LocalPeakTest(unittest.TestCase):
    def test_peak_when_array_has_one_element(self):
        self.assertEqual([2], get_peak([2]))