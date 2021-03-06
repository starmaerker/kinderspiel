import random
import math
from datetime import datetime, timedelta


def calc():
    alpha = datetime.now()
    hours_one = random.randint(0, 23)
    minutes_one = random.randint(0, 60)
    hours_two = random.randint(0, 23)
    minutes_two = random.randint(0, 60)

    first = alpha.replace(hour=hours_one, minute=minutes_one)
    second = alpha.replace(hour=hours_two, minute=minutes_two)

    if first > second:
        first, second = second, first

    delta = second - first

    delta_hours = math.floor(delta.total_seconds() / 3600)
    delta_minutes = math.floor((delta.total_seconds() - delta_hours * 3600) / 60)

    return first.strftime("%H:%M"), second.strftime("%H:%M"), delta_hours, delta_minutes
