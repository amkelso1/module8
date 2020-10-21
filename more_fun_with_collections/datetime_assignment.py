"""
author: Alex Kelso
Date: 10/20/2020

program: datetime_assignment.py
purpose: display and use a real date and time
"""
from datetime import datetime, timedelta


def half_birthday():
    birthday = datetime(2019, 12, 30)
    half_b_day = birthday + timedelta(days=183)
    return 'Half Birthday: ', half_b_day


if __name__ == '__main__':
    print(half_birthday())
