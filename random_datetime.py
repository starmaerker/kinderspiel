import random
from datetime import datetime, timedelta

hours_one = random.randint(0, 23)
minutes_one = random.randint(0, 60)
hours_two = random.randint(0, 23)
minutes_two = random.randint(0, 60)

alpha = datetime.now()

first = alpha.replace(hour=hours_one, minute=minutes_one)
second = alpha.replace(hour=hours_two, minute=minutes_two)

if first > second:
    first, second = second, first

delta = second - first

print(first)
print(second)
print((delta.seconds / 60)//60)
print((delta.seconds / 60) % 60)
