def minSteps(s: str, t: str) -> int:
    sList = s.split('')
    print(sList)
    for i in s:
        for a in t:
            if i == a:
                sList.remove(i)
    return len(sList)


print(minSteps('bab', 'aba'))
