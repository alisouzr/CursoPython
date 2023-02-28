def isIsomorphic(s: str, t: str) -> bool:
    listas = []
    listat = []
    if len(s) != len(t):
        return False
    for i, value in enumerate(s):
        if value in s:
            listas.append(s.index(value))
        if t[i] in t:
            listat.append(t.index(t[i]))
    return True if listas == listat else False


print(isIsomorphic("paper", "title"))
