#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
    return [max(nums) for nums in numbers]


def join_integers(numbers):
    return int("".join(str(num) for num in numbers))


def generate_prime_numbers(limit):
    primes = []
    nums = list(range(2, limit+1))
    while len(nums) > 0:
        primes.append(nums.pop(0))
        nums = list(itertools.filterfalse(lambda x: x % primes[-1] == 0, nums))

    return primes


def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
    permutations = []

    for num in range(1, num_combinations+1):
        isIncluded = True
        if excluded_multiples:
            isIncluded = num % excluded_multiples != 0        
        
        if isIncluded:
            for txt in strings:
                permutations.append(txt + str(num))

    return permutations


if __name__ == "__main__":
    print(get_maximums([[1, 2, 3], [6, 5, 4], [10, 11, 12], [8, 9, 7]]))
    print("")
    print(join_integers([111, 222, 333]))
    print(join_integers([69, 420]))
    print("")
    print(generate_prime_numbers(17))
    print("")
    print(combine_strings_and_numbers(["A", "B"], 2, None))
    print(combine_strings_and_numbers(["A", "B"], 5, 2))
