#What is difference between str() and repr()

# the goal of __repr__ is to be unambiguous
# the goal of __str__ is to be readable

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))

print()

print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))
