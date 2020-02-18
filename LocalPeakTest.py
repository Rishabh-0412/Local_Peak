import unittest


def local_peak_of_list(number):
    if len(number) == 0:
        return None

    else:
        if len(number) == 2:
            if number[0] > number[1]:
                return number[0]
            return number[1]

        elif len(number) >= 3:
            if number[0] > number[1]:
                return number[0]
            return max(number)

        return number[0]


class LocalPeakTest(unittest.TestCase):
    def test_peak_when_array_has_one_element(self):
        self.assertEqual(2, local_peak_of_list([2]))

    def test_peak_when_array_has_two_element(self):
        self.assertEqual(9, local_peak_of_list([9, 1]))

    def test_peak_array_size_3_and_Peak_at_middle(self):
        self.assertEqual(10, local_peak_of_list([9, 10, 2]))

    def test_peak_array_size_3_and_Peak_at_left(self):
        self.assertEqual(19, local_peak_of_list([19, 10, 2]))

    def test_peak_array_size_3_and_Peak_at_left_case2(self):
        self.assertEqual(19, local_peak_of_list([19, 10, 22]))

    def test_peak_array_size_3_and_Peak_at_right(self):
        self.assertEqual(22, local_peak_of_list([9, 10, 22]))

    def test_peak_array_size_3_with_all_elements_equal(self):
        self.assertEqual(19, local_peak_of_list([19, 19, 19]))

    def test_peak_array_size_4_and_Peak_at_left(self):
        self.assertEqual(19, local_peak_of_list([19, 10, 22, 89]))

    def test_peak_array_size_4_and_Peak_at_element2(self):
        self.assertEqual(99, local_peak_of_list([1, 10, 2, 99]))

    def test_peak_null_array(self):
        self.assertEqual(None, local_peak_of_list([]))


if __name__ == '__main__':
    unittest.main()
