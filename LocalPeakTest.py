import unittest


def get_peak(num_list):
    if len(num_list) == 2:
        if num_list[0] > num_list[1]:
            return num_list[0]
        return num_list[1]
    return num_list[0]


class LocalPeakTest(unittest.TestCase):
    def test_peak_when_array_has_one_element(self):
        self.assertEqual(2, get_peak([2]))

    def test_peak_when_array_has_two_element(self):
        self.assertEqual(10, get_peak([9, 10]))