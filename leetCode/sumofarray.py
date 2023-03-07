def runningSum(nums: list[int]) -> list[int]:
    listSum = []
    sum = 0
    for i in nums:
        sum += i
        listSum.append(sum)
    return listSum


print(runningSum([3, 1, 2, 10, 1]))
