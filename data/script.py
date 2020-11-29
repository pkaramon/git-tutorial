from pathlib import Path

print("hello world!!!")


def is_odd(x: int):
    if type(x) is not int:
        raise ValueError("wrong type")
    else:
        return x % 2 == 1


def file_reader(filename: Path):
    if filename.exists():
        readout = filename.open("rt").read()
        return readout
    else:
        raise ValueError("file: {filename} does not exist")
