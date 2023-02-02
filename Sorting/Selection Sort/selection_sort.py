def selectionSort(arr):
    newArr = [] # Ideally of the same size as arr

    for i in range(len(arr)):
        smallest = findSmallest(arr) # Ideally only give a reference to the list and don't copy it over
        newArr.append(arr.pop(smallest))
    return newArr


def findSmallest(arr):
    smallestNumber = arr[0]
    smallestIndex = 0

    for i in range(1, len(arr)):
        currentNum = arr[i]
        if currentNum < smallestNumber:
            smallestNumber = currentNum
            smallestIndex = i
    return smallestIndex


arr = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(selectionSort(arr))