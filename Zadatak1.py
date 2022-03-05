from typing import Counter
from sage.all import *


def take_input():
    while(True):
        try:
            arr_len = Integer(input("How many numbers will you input?"))
            break
        except:
            print("I require an integer")

    input_arr = []
    for value in range(arr_len):
        while(True):
            try:
                int_or_frac = sage.rings.rational.Rational(input())
                input_arr.append(int_or_frac)
                break
            except:
                print("I require an integer or fraction!")
    return input_arr


def filter_arr(arr):
    print(arr)
    return arr


def separate_int_and_fraction(int_and_frac_arr):
    int_and_frac_arr = [sage.rings.rational.Rational(
        element) for element in int_and_frac_arr]
    int_and_frac_arr.sort()
    int_arr = []
    frac_arr = []

    for value in int_and_frac_arr:
        try:
            value = Integer(value)
            int_arr.append(value)
        except TypeError:
            continue

    frac_arr = list((Counter(int_and_frac_arr) - Counter(int_arr)).elements())
    return int_arr, frac_arr


def find_continuous_int_arrays(int_arr):
    first_index = 0
    result_arr = []
    if len(int_arr) == 1:
        return [int_arr]
    for index in range(1, len(int_arr)):
        if (int_arr[index] - int_arr[index - 1] != 1 and int_arr[index] - int_arr[index - 1] != 0):
            result_arr.append(int_arr[first_index: index])
            first_index = index
        if (index == len(int_arr) - 1):
            result_arr.append(int_arr[first_index:])
    return result_arr


def find_continuous_arrays(frac_arr):

    frac_arr = [sage.rings.rational.Rational(element) for element in frac_arr]
    result_arr = []
    partial_arr = []
    distance = 1

    for index1, fraction1 in enumerate(frac_arr):

        partial_arr = [fraction1]
        for fraction2 in frac_arr[index1 + 1:]:
            if (fraction2 - partial_arr[-1] == distance or fraction2 == partial_arr[-1]):
                partial_arr.append(fraction2)

        not_good = False
        for previous_result in result_arr:
            if set(partial_arr) <= set(previous_result):
                not_good = True
        if (not not_good):
            result_arr.append(partial_arr)

    return result_arr


def Exercise1():
    input_arr = take_input()
    divided_arrays = separate_int_and_fraction(input_arr)

    # Option 1 - confirmed by testing to be faster
    continuous_int_arrays = find_continuous_int_arrays(divided_arrays[0])
    # Option 2 - confirmed by testing to be slower
    # continuous_int_arrays = find_continuous_arrays(divided_arrays[0])

    continuous_frac_arrays = find_continuous_arrays(divided_arrays[1])
    return continuous_int_arrays, continuous_frac_arrays

# result = Exercise1()
# print(result)
