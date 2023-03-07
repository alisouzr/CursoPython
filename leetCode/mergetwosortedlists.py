def mergeTwoLists(list1: list, list2: list) -> list:
    lista = []
    lista.extend(list2)
    x = 0
    for i in range(0, len(list1)+2, 2):
        if x < len(list1):
            lista.insert(i, list1[x])
            x += 1
    return lista


print(mergeTwoLists([1, 2, 3], [4, 5, 6]))
