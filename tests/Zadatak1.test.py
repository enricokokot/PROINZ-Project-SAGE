import Zadatak1
import pytest
import sage

def transform_into_arr_of_R(arr):
        transformed = [sage.rings.rational.Rational(element) for element in arr]
        return transformed

def test_separate_int_and_fraction():
        
        Zadatak1.separate_int_and_fraction([1]) == ([1], [])
        Zadatak1.separate_int_and_fraction(
            [-1, 0, 5]) == ([-1, 0, 5], [])
        Zadatak1.separate_int_and_fraction([3]) == ([3], [])
        Zadatak1.separate_int_and_fraction([0, 0, 0]) == ([0, 0, 0], [])
        Zadatak1.separate_int_and_fraction(
            ([12/6, 96/4, 33/3])) == ([2, 11, 24], [])
        Zadatak1.separate_int_and_fraction(
            transform_into_arr_of_R([13/6, 24/5, 99/4])) == (
                [], transform_into_arr_of_R([13/6, 24/5, 99/4]))
        Zadatak1.separate_int_and_fraction([3]) != ([], [3])

        Zadatak1.separate_int_and_fraction(
            [-2, 5, 1/2, 3, 3, 3/2, 4, 3/2, -1, 0, -1/2, 7/2]) == (
                [-2, -1, 0, 3, 3, 4, 5], transform_into_arr_of_R(
                    [-1/2, 1/2, 3/2, 3/2, 7/2]))
        Zadatak1.separate_int_and_fraction(
            [-2, 5, 1/2, -1, 3, 3, 3/2, 4, 3/2, -1, 0, -1/2, -1, 7/2]) != (
                [-2, -1, 0, 3, 3, 4, 5], transform_into_arr_of_R(
                    [-1/2, 1/2, 3/2, 3/2, 7/2]))

test_separate_int_and_fraction()