from time import perf_counter
import BubbleSort
import SelectionSort
import numpy as np
import matplotlib.pyplot as mp

# function to automatically create time duration arrays
# for BubbleSort & SelectionSort
def CreateTimeArrays(ns_parameter = []):
    ns = ns_parameter.copy()
    times_dict = {
        'bubble': [],
        'selection': []
    }

    for t in times_dict.keys():
        for n in ns:
            start = perf_counter()

            if (t == 'bubble'):
                BubbleSort.BubbleSort(np.random.randint(-100, 100, n))
            else:
                SelectionSort.SelectionSortAlt(np.random.randint(-100, 100, n))

            stop = perf_counter()

            times_dict[t].append(stop - start)

    return times_dict

# Function to plot search times of bubble and
# selection sort functions
def PlotSearchTimes():
    # array sizes for the test
    array_of_sizes = [3, 30, 300]

    # create times object/dictionary for plotting
    times_dict = CreateTimeArrays(array_of_sizes)

    # matplotlib work
    axis = mp.subplots()
    axis.scatter(times_dict['bubble'], array_of_sizes, label='Bubble sort', c='r')
    axis.scatter(times_dict['selection'], array_of_sizes, label='Selection sort')
    axis.set_xlabel('Time to sort (ns)')
    axis.set_ylabel('Random array size sorted')
    axis.set_title("Bubble sort vs Selection Sort")
    axis.legend()
    mp.show()

PlotSearchTimes()