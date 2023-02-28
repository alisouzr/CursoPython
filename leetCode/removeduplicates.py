def removeDuplicates(nums: list[int]) -> int:
    left = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[left] = nums[i]
            left += 1

    return left
    """ lista = []
    count = 0
    result = 0
    for i in nums:
        if i not in lista and nums.index(i) != len(nums)-1:
            result += 1
            c = nums.index(i)
            lista.append(i)
        elif i not in lista and nums.index(i) == len(nums)-1:
            result += 1
            lista.append(i)
            c = nums.index(i)
            count += 1
            for i in range(c, (c+count)-1):
                if count > 0:
                    lista.insert(i, "_")
                    count -= 1
        else:
            count += 1
            if nums.index(i) == -len(nums)-1:
                for i in range(c-1):
                    if count > 0:
                        lista.insert(i, "_")
                        count -= 1
    return lista """


print(removeDuplicates([1, 1, 2]))
