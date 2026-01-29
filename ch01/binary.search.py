def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Searching in: {nums[left:right+1]} | Mid: {nums[mid]}")
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1 # if target does not exist

if __name__ == '__main__':
    test_nums, target = [3, 4, 6, 8, 9, 10], 8

    index = binary_search(test_nums, target)
    print(f'Index of the {target}:', index)