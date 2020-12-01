import math
import operator


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def add_vec(u, v):
    return func_vec(u, v, operator.add)


def mul_vec(u, v):
    return func_vec(u, v, operator.mul)


def func_vec(u, v, func):
    if len(u) != len(v):
        raise ValueError("lengths of vectors dont match")
    return [func(x, y) for x, y in zip(u, v)]


def arcsin(angle):
    return math.asin(angle)


def arccos(angle):
    return math.acos(angle)