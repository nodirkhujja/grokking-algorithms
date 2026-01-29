def find_smallest(nums):
    smallest = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
        if smallest > nums[i]:
            smallest = nums[i]
            smallest_index = i
    return smallest_index

def selection_sort(nums):
    result = []
    for _ in range(len(nums)):
        smallest = find_smallest(nums)
        result.append(nums.pop(smallest))
    return result

if __name__ == '__main__':
    test_nums = [23, 12, 55, 9, 3]
    print('Original: ', test_nums)

    sorted = selection_sort(test_nums)
    print('Sorted: ', sorted)
