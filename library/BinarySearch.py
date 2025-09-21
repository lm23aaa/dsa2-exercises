def BinarySearchAction(numbers, target):
    found = False

    while not found and len(numbers) > 0:
        index = int(len(numbers) / 2)

        if numbers[index] == target:
            print(f"I found the number {str(target)} in the list.")
            found = True
            return found
        
        if numbers[index] < target:
            numbers = numbers[(index + 1):len(numbers)]

        elif numbers[index] > target:
            numbers = numbers[0:index]
    
    print(f"Number {str(target)} was not found in the sorted list of numbers.")
    return found

def BinarySearch():
    numbers = [int(s) for s in input("Please enter a comma separated, sorted list of integers i.e. -1,0,3,4,56 etc: ").split(',')]
    target = int(input("Please enter an integer to find in the sorted list: "))

    return BinarySearchAction(numbers, target)