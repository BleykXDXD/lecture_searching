import os
import json
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
    for idx, value in enumerate(field):
        if value == number:
            seznam.append(idx)
            count += 1
    return {"Positions": seznam, "Count": count}





def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    sequential_data1 = read_data("sequential.json", "ordered_numbers")
    sequential_data2 = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    print(linear_search([54, 2, 18, 5, 3, 31, 20, 65, -10, 300, 17, 5, -1, 0, 0, 102, 7, 8, 9, 9, -3, -5, 0, 1, 63, 82, -36, -5], 9))



if __name__ == '__main__':
    main()