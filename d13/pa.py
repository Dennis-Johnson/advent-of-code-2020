from math import ceil

prompt = open('input.txt', 'r').readlines()

earliest_ts = int(prompt[0])
buses = [int(id) for id in prompt[1].strip().split(',') if id != 'x']

closest_multiple = [x * ceil(earliest_ts / x) for x in buses]
wait_time = min(closest_multiple) - earliest_ts
bus_id = buses[closest_multiple.index(min(closest_multiple))]

print("BusID * wait_time = {} * {} = {}".format(bus_id, wait_time, bus_id * wait_time))
