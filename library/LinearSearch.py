def LinearSearchAction(list, target):
    numbers = list.copy()
    
    for i in range (0,len(numbers)):
        if numbers[i]==target:
            print(f"I found the number {str(target)} in the index {str(i)} of the list.")
            return i
    
    print(f"Number {str(target)} was not found in the list of numbers.")
    return -1

def LinearSearch():
    numbers = [int(s) for s in input("Please enter a comma separated, list of integers i.e. -1,0,3,4,56 etc: ").split(',')]
    target = int(input("Please enter an integer to find in the list: "))

    return LinearSearchAction(numbers, target)
