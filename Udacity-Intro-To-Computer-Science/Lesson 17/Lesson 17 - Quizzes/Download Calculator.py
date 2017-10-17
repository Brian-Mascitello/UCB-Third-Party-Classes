# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

# print(2 ** 10)  # one kilobit, kb
# print(2 ** 10 * 8)  # one kilobyte, kB
#
# print(2 ** 20)  # one megabit, Mb
# print(2 ** 20 * 8)  # one megabyte, MB
#
# print(2 ** 30)  # one gigabit, Gb
# print(2 ** 30 * 8)  # one gigabyte, GB
#
# print(2 ** 40)  # one terabit, Tb
# print(2 ** 40 * 8)  # one terabyte, TB

bits_dictionary = dict()
bits_dictionary['kb'] = 2.0 ** 10
bits_dictionary['kB'] = 2.0 ** 10 * 8
bits_dictionary['Mb'] = 2.0 ** 20
bits_dictionary['MB'] = 2.0 ** 20 * 8
bits_dictionary['Gb'] = 2.0 ** 30
bits_dictionary['GB'] = 2.0 ** 30 * 8
bits_dictionary['Tb'] = 2.0 ** 40
bits_dictionary['TB'] = 2.0 ** 40 * 8


def convert_seconds(input_seconds):
    return_string = ''

    hours = int(input_seconds / 3600)
    hours_text = ' hours, ' if hours != 1 else ' hour, '
    return_string += str(hours) + hours_text

    seconds_after_hours = input_seconds % 3600
    minutes = int(seconds_after_hours / 60)
    minutes_text = ' minutes, ' if minutes != 1 else ' minute, '
    return_string += str(minutes) + minutes_text

    seconds = seconds_after_hours % 60
    seconds_text = ' seconds' if seconds != 1 else ' second'
    return_string += str(seconds) + seconds_text
    return return_string


# Often bandwidth is given in megabits (Mb) per second whereas file size
# is given in megabytes (MB).

def download_time(file_size, file_size_units, bandwidth, bandwidth_unit_size):
    file_size_bits = file_size * bits_dictionary[file_size_units]
    bandwidth_bits = bandwidth * bits_dictionary[bandwidth_unit_size]
    transfer_in_seconds = file_size_bits / bandwidth_bits
    return convert_seconds(transfer_in_seconds)


print(download_time(1024, 'kB', 1, 'MB'))
# >>> 0 hours, 0 minutes, 1 second

print(download_time(1024, 'kB', 1, 'Mb'))
# >>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print(download_time(13, 'GB', 5.6, 'MB'))
# >>> 0 hours, 39 minutes, 37.1428571429 seconds

print(download_time(13, 'GB', 5.6, 'Mb'))
# >>> 5 hours, 16 minutes, 57.1428571429 seconds

print(download_time(10, 'MB', 2, 'kB'))
# >>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print(download_time(10, 'MB', 2, 'kb'))
# >>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable

print(download_time(11, 'GB', 5, 'MB'))
# >>> 0 hours, 37 minutes, 32.8 seconds
