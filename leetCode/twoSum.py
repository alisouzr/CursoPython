def twoSum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for a in range(i+1, len(nums)):
            if nums[a] == target - nums[i]:
                return [i, a]


print(twoSum([3, 2, 4], 6))
