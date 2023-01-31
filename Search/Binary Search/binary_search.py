# Array initilization from 1 to 10 Million

def init_array(n: int):
    arr = []
    for i in range(n +1):
        arr.append(i)
    return arr

def binary_search(num_to_find, array_length=50):
    steps = 0
    arr = init_array(array_length)

    low = 0
    high = len(arr) -1

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        current_element = arr[mid]
        if current_element == num_to_find:
            return mid, steps
        elif current_element < num_to_find:
            low = mid + 1
        elif current_element > num_to_find:
            high = mid - 1
    return None, steps

n = 100
element_to_find = 200
index, steps = binary_search(element_to_find, n)
print(f"It took {steps} steps to find '{element_to_find}' in a list with {n} Elements.\nIndex is at {index}")