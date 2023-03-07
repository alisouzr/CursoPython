def is_valid_walk(walk):
    # determine if walk is valid
    ns = 0
    ew = 0
    if len(walk) == 10:
        for i in walk:
            if i == 'n':
                ns += 1
            if i == 's':
                ns -= 1
            if i == 'w':
                ew += 1
            if i == 'e':
                ew -= 1
    else:
        return False
    return ns == 0 and ew == 0


print(is_valid_walk(['w', 'e', 'w', 'e', 'w',
      'e', 'w', 'e', 'w', 'e']))
