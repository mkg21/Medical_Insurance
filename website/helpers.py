import datetime
from collections import namedtuple
from dataclasses import dataclass
from datetime import date


def struct(data: dict):
    try:
        return namedtuple('Struct', data.keys())(*data.values())
    except:
        return data


def age(birthdate: datetime.date):
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))