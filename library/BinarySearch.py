def BinarySearchOriginal(list_parameter = [], target = 0):
    if (len(list_parameter) == 0):
        print(f"Number {str(target)} was not found in the sorted list of numbers.")
        return -1
    
    found = False
    numbers = list_parameter.copy()

    while not found and len(numbers) > 0:
        index = int(len(numbers) / 2)
        middle_item = int(numbers[index])

        if middle_item == target:
            print(f"I found the number {str(target)} in the list.")
            found = True
            return found
        
        if middle_item < target:
            numbers = numbers[index:]

        elif middle_item > target:
            numbers = numbers[:index]
    
    print(f"Number {str(target)} was not found in the sorted list of numbers.")
    return found

def BinarySearch(list_parameter = [], target = 0):
    """
    Returns the index of a number if it is present in an SORTED list of
    ints, using the binary search algorith.
    E.g         valid   BinarySearch([1,2,4],4) = 2
                        BinarySearch([-1,0,3,4,56],0) = 1
                invalid BinarySearch([],5) = -1
                        BinarySearch([-1,0,3,4,56],70) = -1
    @param      list_paramter, SORTED list of ints
    @param      target, int which is the taget value of the search
    @returns    index value of the target in the array, or -1 if the value
                is not present, or if the list_parameter is empty
    """

    if (len(list_parameter) == 0):
        print(f"Number {str(target)} was not found in the sorted list of numbers.")
        return -1

    start = 0
    end = len(list_parameter) - 1

    while start <= end:
        middle = int((start + end) / 2)
        curr = int(list_parameter[middle])

        if curr == target:
            print(f"I found {str(target)} at index {str(middle)} in the list.")
            return middle
        
        if curr < target:
            start = middle + 1

        elif curr > target:
            end = middle - 1
    
    print(f"Number {str(target)} was not found in the sorted list of numbers.")
    return -1

def BinarySearchUserInput():
    numbers = input("Please enter a comma separated, sorted list of integers i.e. -1,0,3,4,56 etc: ").split(',')
    target = int(input("Please enter an integer to find in the sorted list: "))

    return BinarySearch(numbers, target)