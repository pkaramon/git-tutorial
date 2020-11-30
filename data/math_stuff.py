def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def add_vec(u, v):
    if len(u) != len(v):
        raise ValueError("lengths of vectors dont match")
    return [x + y for x, y in zip(u, v)]
