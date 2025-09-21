def SelectionSort(list_parameter):
    # Based on psuedocode from DSA2 2.4, amended to sort by asc alphabetically,
    # or asc numerically
    # https://herts.instructure.com/courses/123373/pages/2-dot-4-sorting-algorithms
    list = list_parameter.copy()
    result = []
    n = len(list)
    number_of_steps = 0

    for i in range(0, n):
        minimum_element = list[0]

        for j in range(0, n):
            if (list[j] < minimum_element):
                minimum_element = list[j]

            number_of_steps = number_of_steps + 1

        result.append(minimum_element)
        list.remove(minimum_element)
        n -= 1
    
    print(result)
    # print(number_of_steps)
    return result

def SelectionSortAlt(list):
    # Based on psuedocode from DSA1 6.2.2, sorting by asc alphabetically,
    # or asc numerically
    # https://herts.instructure.com/courses/118171/pages/6-dot-2-2-selection-sort
    n = 0
    number_of_steps = 0
    list = list.copy()

    while n < len(list) - 1:
        for i in range(n + 1, len(list)):
            if list[n] > list[i]:
                list[n], list[i] = list[i], list[n]

            number_of_steps = number_of_steps + 1
        n += 1
    
    print(list)
    # print(number_of_steps)
    return list

def SelectionSortWordLength(list):
    # Based on psuedocode from DSA1 6.2.2, sorting by asc word length
    # https://herts.instructure.com/courses/118171/pages/6-dot-2-2-selection-sort
    list = list.copy()
    result = []
    n = len(list)
    number_of_steps = 0

    for i in range(0, n):
        minimum_length = len(list[0])
        minimum_element = list[0]
        
        for j in range(0, n):
            if (len(list[j]) < minimum_length):
                minimum_length = len(list[j])
                minimum_element = list[j]

            number_of_steps = number_of_steps + 1

        result.append(minimum_element)
        list.remove(minimum_element)
        n = n - 1

    print(result)
    # print(number_of_steps)
    return result

# TESTING BELOW
# list = ["London", "Canterbury", "York", "Leicester"]
# list = [3, 1, 4, 2]
# list = [0.5,0.01,0.001,0.0001,0.7,0.02]
# SelectionSortAlt(list)
# SelectionSort(list)
# SelectionSortWordLength(list)