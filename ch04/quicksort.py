def quicksort(array):
    if len(array) < 2:
        return array  # base case: arrays with 0 or 1 element are already "sorted"
    else:
        pivot = array[0]  # recursive case      
        less = [i for i in array[1: ] if i <= pivot]  # sub-array: less than pivot

        greater = [i for i in array[1: ] if i > pivot]  # sub-array: greater than pivot

        return quicksort(less) + [pivot] + quicksort(greater)
    
if __name__ == '__main__':
    test_array = [33, 10, 15, 7]
    print(f"Original: {test_array}")

    sorted_array = quicksort(test_array)
    print(f"Sorted: {sorted_array}")
