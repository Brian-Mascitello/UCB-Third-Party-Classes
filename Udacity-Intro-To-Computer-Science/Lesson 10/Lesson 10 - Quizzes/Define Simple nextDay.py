#
# Define a simple nextDay procedure, that assumes
# every month has 30 days.
#
# For example:
#    nextDay(1999, 12, 30) => (2000, 1, 1)
#    nextDay(2013, 1, 30) => (2013, 2, 1)
#    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
#

# DID NOT ACCOUNT FOR EVERY MONTH HAVING 30 DAYS
# from datetime import datetime
# from datetime import timedelta
#
#
# def nextDay(year, month, day):
#     """
#     Returns the year, month, day of the next day.
#     Simple version: assume every month has 30 days.
#     """
#
#     tomorrow = datetime(year=year, month=month, day=day) + timedelta(days=1)
#
#     return tomorrow.year, tomorrow.month, tomorrow.day
#


def nextDay(year, month, day):
    """
    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """

    if month == 12 and day == 30:
        year += 1
        month = 1
        day = 1
    elif day == 30:
        month += 1
        day = 1
    else:
        day += 1

    return year, month, day


# Tests
print(nextDay(2017, 10, 11))
# (2017, 10, 12)

print(nextDay(1989, 3, 24))
# (1989, 3, 25)

print(nextDay(2015, 12, 31))
# (2016, 1, 1)
