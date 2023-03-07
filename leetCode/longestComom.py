def longestCommonPrefix(strs: list[str]) -> str:
    less = min(strs, key=len)
    for item in strs:
        while len(less) > 0:
            if item.startswith(less):
                break
            else:
                less = less[:-1]
    return less


print(longestCommonPrefix(["flower", "flow", "flight"]))
