import os
import json
import time
from random import choices

import matplotlib.pyplot as plt
# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as f:
        data = json.load(f)
        if field in data:
            return data[field]


def linear_search(field, number):
    seznam = []
    count = 0
    start = time.perf_counter()
    for idx, value in enumerate(field):
        if value == number:
            seznam.append(idx)
            count += 1
    end = time.perf_counter()

    duration = end - start
    return duration
    return {"Positions": seznam, "Count": count}

def binary_search(field, number):
    left = 0
    right = len(field) - 1
    start = time.perf_counter()
    while left <= right:
        mid = (left + right) // 2
        middle_value = field[mid]

        if number < middle_value:
            right = mid - 1
        elif number > middle_value:
            left = mid + 1
        else:
            return mid
    end = time.perf_counter()

    return end - start
    return None




def unordered_sequence(max_len=100):
    """
    Returns list of unordered ints from within a range between -1000 and 1000.
    :param max_len: (int) desired length of sequence
    :return: (list) sequence of numbers
    """
    return choices(range(-1000, 1000), k=max_len)




def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    sequential_data1 = read_data("sequential.json", "ordered_numbers")
    sequential_data2 = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    print(linear_search([54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5], 9))
    print(binary_search(sequential_data1,13))



if __name__ == '__main__':
    main()