def distinct(seq):
    b = []
    [b.append(item) for item in seq if item not in b]
    return b
    pass


def distinct2(seq):
    b = list(set(seq))
    return b
    pass
