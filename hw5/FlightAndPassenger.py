"""
result example:
    01/2006, Arrival, Domestic, 51, 19748
    01/2006, Arrival, International, 75, 20383
    01/2006, Departure, Domestic, 79, 19388
"""

from pyspark import SparkContext


def parse_time(prev_time):
    # 01/01/2006 12:00:00 AM
    time = prev_time.split()[0]
    year, month = time.split('/')[2], time.split('/')[0]
    return "{}/{}".format(month, year)


def parse_flight(csv_line):
    flight_info = csv_line.split(',')
    flight_time = parse_time(flight_info[1])
    flight_type = flight_info[3]
    flight_region = flight_info[4]
    cur_key = (flight_time, flight_type, flight_region)  # use tuple as key
    flight_count = int(flight_info[5])
    return cur_key, [flight_count, 0]


def parse_passenger(csv_line):
    pass_info = csv_line.split(',')
    pass_time = parse_time(pass_info[1])
    pass_type = pass_info[3]
    pass_region = pass_info[4]
    cur_key = (pass_time, pass_type, pass_region)  # use tuple as key
    pass_count = int(pass_info[5])
    return cur_key, [0, pass_count]


sc = SparkContext(appName="inf551")
csv = sc.textFile('lax_flights.csv')

counts = csv \
    .map(parse_flight) \
    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
    .sortByKey(False)

csv_2 = sc.textFile('lax_passengers.csv')

counts_2 = csv_2 \
    .map(parse_passenger) \
    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
    .sortByKey(False)

total_count = counts + counts_2

final_res = total_count \
    .reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])) \
    .sortByKey(False)

for v in final_res.collect():
    print v[0][0], v[0][1], v[0][2], v[1][0], v[1][1]
    # print '%s, %s' % (v[0], v[1])
