import numpy as np
from time import perf_counter

def bogosort(arr: list[int]) -> bool:
    if (sorted_check(arr)):
        return True
    
    arr_copy = arr.copy()
    np.random.shuffle(arr_copy)

    return sorted_check(arr_copy)

def bogosort_lasvegas(arr: list[int]) -> bool:
    if (sorted_check(arr)):
        return True
    
    arr_copy = arr.copy()
    should_stop_loop = False

    while should_stop_loop == False:
        np.random.shuffle(arr_copy)
        should_stop_loop = sorted_check(arr_copy)

    return should_stop_loop

def sorted_check(arr: list[int]) -> bool:
    sorted = True

    for i in range(0, len(arr) - 1):
        if i + 1 != len(arr) and arr[i] < arr[i + 1]:
            continue
        else:
            sorted = False
            break

    return sorted

# TASK 1
# true_array = []
# arr = [5, 2, 4, 3, 1]

# for i in range(1, 1001):
#     if (bogosort(arr)):
#         true_array.append(1)

# true_count = len(true_array)

# if true_count > 0:
#     print(f"bogosort function success rate {true_count}/1000 = {true_count/1000}")
# else:
#     print(f"bogosort function did not have a successful run")
# TASK 1 END

# TASK 2
arr = [5, 2, 4, 3, 1]
start = perf_counter()
bogosort_lasvegas(arr)
stop = perf_counter()
print(f"las vegas bogosort tool {stop - start} to sort the array")
# TASK 2 END