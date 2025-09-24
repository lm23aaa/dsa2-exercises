def LinearSearch(numbers, target):
    for i in range (0, len(numbers)):
        if int(numbers[i]) == target:
            print(f"I found the number {str(target)} in the index {str(i)} of the list.")
            return i
    
    print(f"Number {str(target)} was not found in the list of numbers.")
    return -1

def LinearSearchUserInput():
    numbers = input("Please enter a comma separated, list of integers i.e. -1,0,3,4,56 etc: ").split(',')
    target = int(input("Please enter an integer to find in the list: "))

    return LinearSearch(numbers, target)
