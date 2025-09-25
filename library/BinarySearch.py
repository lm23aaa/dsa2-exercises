def BinarySearch(list_parameter, target):
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

def BinarySearchUserInput():
    numbers = input("Please enter a comma separated, sorted list of integers i.e. -1,0,3,4,56 etc: ").split(',')
    target = int(input("Please enter an integer to find in the sorted list: "))

    return BinarySearch(numbers, target)