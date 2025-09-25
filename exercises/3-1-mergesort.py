# 1. merge sort
def mergesort(array):
    if len(array) <= 1:
        return array
    else:
        index = int(len(array) / 2)
        array_left = array[:index]
        array_right = array[index:]
        return merge_arrays(mergesort(array_left), mergesort(array_right))

def merge_arrays(array1, array2):
    merged_arrays = []
    i, j = 0, 0

    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            merged_arrays.append(array1[i])
            i += 1
        else:
            merged_arrays.append(array2[j])
            j += 1

    if (i < len(array1)):
        merged_arrays += array1[i:]
        
    if (j < len(array2)):
        merged_arrays += array2[j:]
        
    return merged_arrays

# TEST 1.
# print(mergesort([8,3,5,1,45,234,6,2,11]))