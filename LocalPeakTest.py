import unittest


def get_peak(num_list):
    if len(num_list) == 2:
        if num_list[0] > num_list[1]:
            return num_list[0]
        return num_list[1]

    elif len(num_list) == 3:
        if num_list[0] > num_list[1] and num_list[0] > num_list[2]:
            return num_list[0]
        elif num_list[2] > num_list[1] and num_list[2] > num_list[0]:
            return num_list[2]
        return num_list[1]

    return num_list[0]


class LocalPeakTest(unittest.TestCase):
    def test_peak_when_array_has_one_element(self):
        self.assertEqual(2, get_peak([2]))

    def test_peak_when_array_has_two_element(self):
        self.assertEqual(9, get_peak([9, 1]))

    def test_peak_array_size_3_and_Peak_at_middle(self):
        self.assertEqual(10, get_peak([9, 10, 2]))

    def test_peak_array_size_3_and_Peak_at_left(self):
        self.assertEqual(19, get_peak([19, 10, 2]))