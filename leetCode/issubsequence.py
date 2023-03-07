def isSubsequence(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    if len(s) == 0:
        return True
    sequence = 0
    for i in range(0, len(t)):
        if sequence <= len(s) - 1:
            if s[sequence] == t[i]:
                sequence += 1
    return sequence == len(s)


print(isSubsequence("abc", "agrtbwyxc"))
