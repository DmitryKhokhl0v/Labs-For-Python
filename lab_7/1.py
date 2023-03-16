import numpy as np
import time
import random


def difference():
    num_of_elements = 10 ** 6

    # NumPy
    arr_np1 = np.random.randint(0, 99999, num_of_elements)
    arr_np2 = np.random.randint(0, 99999, num_of_elements)

    # Lists
    list1 = list2 = []
    for i in range(num_of_elements):
        list1.append(random.randint(0, 99999))
        list2.append(random.randint(0, 99999))

    # NumPy
    start_np = time.perf_counter()
    np_composition = np.multiply(arr_np1, arr_np2)
    all_time_np = time.perf_counter() - start_np

    # Lists
    start_list = time.perf_counter()
    list_composition = []
    for i in range(num_of_elements):
        list_composition.append(list1[i] * list2[i])
    all_time_list = time.perf_counter() - start_list

    print("C Numpy: ", all_time_np)
    print("Без Numpy: ", all_time_list)
    print("Разница: ", all_time_list - all_time_np)


difference()
