import Zadatak1
from unittest import mock, TestCase
import numpy as np
import sage

# TODO: make tests readable, remove redundancies


class Test_Zadatak1(TestCase):
    thousand_element_arr_of_2 = np.full(1000, 2)
    thousand_element_arr_of_2 = thousand_element_arr_of_2.tolist()

    unfiltered_inputs = {
        "zero input": ['0'],
        "clean int input": ['5', '1', '2', '3', '4', '5'],
        "dirty input": ['1', 'w', 'a', 's', 'd', '0'],
        "very dirty input": ['a', 'b', 'c', '4', '66/6', '2/3', '15', 'e', 'g', '21777'],
    }

    clean_arrays = {
        "empty": [],
        "zero": [0],
        "sorted 5": [1, 2, 3, 4, 5],
        "mixed": [11, 2/3, 15, 21777],
    }

    def transform_into_arr_of_R(self, arr):
        transformed = [sage.rings.rational.Rational(
            element) for element in arr]
        return transformed

    @mock.patch('builtins.input')
    def test_input(self, mocked_input):
        mocked_input.side_effect = self.unfiltered_inputs["zero input"]
        self.assertEqual(Zadatak1.take_input(),
                         self.clean_arrays["empty"])
        mocked_input.side_effect = self.unfiltered_inputs["dirty input"]
        self.assertEqual(Zadatak1.take_input(),
                         self.clean_arrays["zero"])
        mocked_input.side_effect = self.unfiltered_inputs["clean int input"]
        self.assertEqual(Zadatak1.take_input(),
                         self.clean_arrays["sorted 5"])
        mocked_input.side_effect = self.unfiltered_inputs["very dirty input"]
        self.assertEqual(Zadatak1.take_input(),
                         self.transform_into_arr_of_R(self.clean_arrays["mixed"]))

    def test_separate_int_and_fraction(self):

        self.assertEqual(Zadatak1.separate_int_and_fraction([0]), ([0], []))
        self.assertEqual(Zadatak1.separate_int_and_fraction(
            [-1, 0, 5]),
            (self.transform_into_arr_of_R([-1, 0, 5]), []))
        self.assertEqual(Zadatak1.separate_int_and_fraction([3]), ([3], []))
        self.assertEqual(Zadatak1.separate_int_and_fraction(
            [0, 0, 0]), ([0, 0, 0], []))
        self.assertEqual(Zadatak1.separate_int_and_fraction(
            ([12/6, 96/4, 33/3])),
            ([2, 11, 24], []))
        self.assertEqual(Zadatak1.separate_int_and_fraction(
            self.transform_into_arr_of_R([13/6, 24/5, 99/4])),
            ([], self.transform_into_arr_of_R([13/6, 24/5, 99/4])))
        self.assertFalse(Zadatak1.separate_int_and_fraction([3]) == ([], [3]))

        self.assertEqual(Zadatak1.separate_int_and_fraction(
            [-2, 5, 1/2, 3, 3, 3/2, 4, 3/2, -1, 0, -1/2, 7/2]),
            ([-2, -1, 0, 3, 3, 4, 5], self.transform_into_arr_of_R([-1/2, 1/2, 3/2, 3/2, 7/2])))
        self.assertFalse(Zadatak1.separate_int_and_fraction(
            [-2, 5, 1/2, -1, 3, 3, 3/2, 4, 3/2, -1, 0, -1/2, -1, 7/2]) ==
            ([-2, -1, 0, 3, 3, 4, 5], self.transform_into_arr_of_R([-1/2, 1/2, 3/2, 3/2, 7/2])))

    def test_find_continuous_int_arrays(self):

        self.assertEqual(Zadatak1.find_continuous_int_arrays([1]), [[1]])
        self.assertEqual(Zadatak1.find_continuous_int_arrays(
            [4, 4, 4]), [[4, 4, 4]])
        self.assertEqual(Zadatak1.find_continuous_int_arrays(
            [1, 2, 3, 5, 6, 7, 9, 10, 11]),
            [[1, 2, 3], [5, 6, 7], [9, 10, 11]])
        self.assertEqual(Zadatak1.find_continuous_int_arrays(
            [-2, -1, 0, 3, 3, 4, 5]),
            [[-2, -1, 0], [3, 3, 4, 5]])
        self.assertEqual(Zadatak1.find_continuous_int_arrays(
            [-1/2, 1/2, 3/2, 3/2, 7/2]),
            [[-1/2, 1/2, 3/2, 3/2], [7/2]])

    def test_find_continuous_frac_arrays(self):
        self.assertEqual(Zadatak1.find_continuous_arrays(
            [1/4]),
            [self.transform_into_arr_of_R([1/4])])
        self.assertEqual(Zadatak1.find_continuous_arrays(
            [1/12, 1/12, 1/12]),
            [self.transform_into_arr_of_R([1/12, 1/12, 1/12])])
        self.assertEqual(Zadatak1.find_continuous_arrays(
            [9/13, 12/13, 22/13, 25/13]),
            [self.transform_into_arr_of_R([9/13, 22/13]),
             self.transform_into_arr_of_R([12/13, 25/13])])
        self.assertEqual(Zadatak1.find_continuous_arrays(
            [-3/5, -2/5, -1/5, 1/5, 2/5, 3/5]),
            [self.transform_into_arr_of_R([-3/5, 2/5]),
             self.transform_into_arr_of_R([-2/5, 3/5]),
             self.transform_into_arr_of_R([-1/5]),
             self.transform_into_arr_of_R([1/5])])

    @mock.patch('builtins.input')
    def test_whole_exercise(self, mocked_input):

        mocked_input.side_effect = [12, -2, 5, 1 /
                                    2, 3, 3, 3/2, 4, 3/2, -1, 0, -1/2, 7/2]
        self.assertEqual(Zadatak1.Exercise1(),
                         ([[-2, -1, 0], [3, 3, 4, 5]],
                          [self.transform_into_arr_of_R([-1/2, 1/2, 3/2, 3/2]),
                           self.transform_into_arr_of_R([7/2])]))

        mocked_input.side_effect = [0]
        self.assertEqual(Zadatak1.Exercise1(), ([], []))

        mocked_input.side_effect = [1, 1]
        self.assertEqual(Zadatak1.Exercise1(), ([[1]], []))

        mocked_input.side_effect = [8, 9, 12, -5, -1, 3, -4, 0, 1]
        self.assertEqual(Zadatak1.Exercise1(),
                         ([[-5, -4], [-1, 0, 1], [3], [9], [12]], []))

        mocked_input.side_effect = [
            12, 80, 12, -5, 3, 4, 79, 8, 3, 4, 2, 13, 25]
        self.assertEqual(
            Zadatak1.Exercise1(),
            ([[-5], [2, 3, 3, 4, 4], [8], [12, 13], [25], [79, 80]], []))

        mocked_input.side_effect = [
            'a', 'e', 'r', 12, 80, 'k', 12, -5, 3, 4, 'nj', 79, 8, 3, 4, 2, 'd', 13, 25]
        self.assertEqual(
            Zadatak1.Exercise1(),
            ([[-5], [2, 3, 3, 4, 4], [8], [12, 13], [25], [79, 80]], []))

        mocked_input.side_effect = [
            9, -7, 11/5, 4/7, 8/5, -3, -1/2, 16/5, 20, 21]
        self.assertEqual(
            Zadatak1.Exercise1(),
            ([[-7], [-3], [20, 21]],
             [self.transform_into_arr_of_R([-1/2]),
             self.transform_into_arr_of_R([4/7]),
             self.transform_into_arr_of_R([8/5]),
             self.transform_into_arr_of_R([11/5, 16/5])]))

        mocked_input.side_effect = [
            'a', 'e', 'r', 6, 'k', 74/95, 13/9, 'nj', 21/8, 16/5, 'd', 11/5, 39/4]
        self.assertEqual(
            Zadatak1.Exercise1(),
            ([],
             [self.transform_into_arr_of_R([74/95]),
             self.transform_into_arr_of_R([13/9]),
             self.transform_into_arr_of_R([11/5, 16/5]),
             self.transform_into_arr_of_R([21/8]),
             self.transform_into_arr_of_R([39/4])]))

        mocked_input.side_effect = [
            'a', 9, -1000, 'b', 17/10, 'c', 1/2, 13/9, 'd', 27/10, 3/2, 'e', -1/2, 37/10, 22/9]
        self.assertEqual(
            Zadatak1.Exercise1(),
            ([[-1000]],
             [self.transform_into_arr_of_R([-1/2, 1/2, 3/2]),
             self.transform_into_arr_of_R([13/9, 22/9]),
             self.transform_into_arr_of_R([17/10, 27/10, 37/10])]))

        mocked_input.side_effect = [
            5, -10007/10, -1000, -1001, -10004/10, -9997/10]
        self.assertEqual(
            Zadatak1.Exercise1(),
            ([[-1001, -1000]],
             [self.transform_into_arr_of_R([-10007/10, -9997/10]),
             self.transform_into_arr_of_R([-5002/5])]))

        mocked_input.side_effect = [1000] + self.thousand_element_arr_of_2
        self.assertEqual(Zadatak1.Exercise1(),
                         ([self.thousand_element_arr_of_2], []))

    def test_filter_arr(self):
        Zadatak1.filter_arr([
            5, -10007/10, -1000, -1001, -10004/10, -9997/10]),
        ([[-1001, -1000]],
         [self.transform_into_arr_of_R([-10007/10, -9997/10]),
         self.transform_into_arr_of_R([-5002/5])])

# Test_Zadatak1().test_input()
# Test_Zadatak1().test_separate_int_and_fraction()
# Test_Zadatak1().test_find_continuous_int_arrays()
# Test_Zadatak1().test_find_continuous_frac_arrays()
# Test_Zadatak1().test_whole_exercise()
