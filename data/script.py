from pathlib import Path

print("hello world!!!")


def is_odd(x: int):
    if type(x) is not int:
        raise ValueError("wrong type")
    else:
        return x % 2 == 1


def is_even(x: int):
    return not is_odd(x)


class Person:
    def __init__(self, name: str, age: int, married: bool):
        self._age = age
        self._name = name
        self.married = married

    @property
    def name(self):
        return self._name.capitalize()

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if type(value) is int and value >= self._age:
            self._age = value
        else:
            raise ValueError("invalid age: {value}")


def file_reader(filename: Path):
    if filename.exists():
        readout = filename.open("rt").read()
        return readout
    else:
        raise ValueError("file: {filename} does not exist")
