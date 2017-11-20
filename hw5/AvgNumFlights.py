"""
result example:
    2006, arrival, 207
    2006, departure, 302

"""
from operator import add

from pyspark import SparkContext


def parse_time(prev_time):
    # 01/01/2006 12:00:00 AM
    time = prev_time.split()[0]
    year = time.split('/')[2]
    return year


def parse_flight(csv_line):
    flight_info = csv_line.split(',')
    flight_time = parse_time(flight_info[1])
    flight_type = flight_info[3]
    flight_count = int(flight_info[5])
    cur_key = (flight_time, flight_type)
    return cur_key, flight_count


sc = SparkContext(appName="inf551")
csv = sc.textFile('lax_flights.csv')
# rows = csv.flatMap(lambda x: x.split(','))

counts = csv \
    .map(parse_flight) \
    .reduceByKey(add) \
    .mapValues(lambda x: x / 12)
#   .sortByKey(False)

for v in counts.collect():
    print v[0][0], v[0][1], v[1]
    # print '%s, %s' % (v[0], v[1])
