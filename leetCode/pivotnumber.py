def pivotIndex(nums):
    Sum = sum(nums)
    left = 0
    for i, value in enumerate(nums):
        if left == (Sum - left - value):
            return i
        left += value
    return -1


print(pivotIndex([1, 7, 3, 6, 5, 6]))
