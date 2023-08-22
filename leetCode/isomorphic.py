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


<<<<<<< HEAD
print(isIsomorphic("paper", "title"))
=======
print(isIsomorphic("lente", "dente"))
>>>>>>> bce93cd1dbdbcb75d1a637af8d525cf52349f1d9
