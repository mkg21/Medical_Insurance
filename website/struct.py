from collections import namedtuple


def struct(data: dict):
    try:
        return namedtuple('Struct', data.keys())(*data.values())
    except:
        return data



