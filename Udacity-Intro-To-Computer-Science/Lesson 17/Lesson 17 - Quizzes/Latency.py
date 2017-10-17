# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000.0  # km per second


def speed_fraction(time_in_ms, distance_data):
    full_distance_traceroute = distance_data * 2
    data_km_s = 1000.0 / time_in_ms * full_distance_traceroute  # 1000.0 ms per s
    speed_of_data = data_km_s / speed_of_light
    return speed_of_data


print(speed_fraction(50, 5000))
# >>> 0.666666666667

print(speed_fraction(50, 10000))
# >>> 1.33333333333  # Any thoughts about this answer, or these inputs?
