def BubbleSort(list):
    has_swapped = True

    while (has_swapped == True):
        has_swapped = False

        for i in range(0, len(list)):
            if i + 1 != len(list) and list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                has_swapped = True
    
    print(list)
    return list

# TESTING BELOW
# BubbleSort(["London", "Canterbury", "York", "Leicester"])
# BubbleSort([3,4,90,75,382,2,8,3,55,32,1,19,0,11])
# BubbleSort([0.5,0.01,0.001,0.0001,0.7,0.02])