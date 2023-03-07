def isValid(s: str) -> bool:
    lista = []
    thereis = {')': '(', '}': '{', ']': '['}

    for i in s:
        if i in thereis.values():
            lista.append(i)
        elif lista and thereis[i] == lista[-1]:
            lista.pop()
        else:
            return False

    return lista == []


print(isValid("([)]"))
