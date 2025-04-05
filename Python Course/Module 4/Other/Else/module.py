import sys
location = sys.path
print(location)
for i in location:
    print(i)

import calendar
def example():
    print(calendar.leapdays(2019,2100))
    print(calendar.isleap(2020))