import csv
from operator import add

from pyspark import SparkContext


def parse_time(prev_time):
    # 01/01/2006 12:00:00 AM
    time = prev_time.split()[0]
    month, year = time.split('/')[0], time.split('/')[2]
    return '{}/{}'.format(month, year)


def parse_vals(line):
    # x = x.split(',')
    vals = line.split(',')
    filter_terminals = ['Imperial Terminal', 'Misc. Terminal']
    time = parse_time(vals[1])
    terminal = vals[2]
    pass_count = vals[5]

    if terminal not in filter_terminals:
        return (time, pass_count)
    else:
        return (time, 0)  # not count passengers from the other terminals


sc = SparkContext(appName="inf551")

filter_terminals = ['Imperial Terminal', 'Misc. Terminal']
with open('lax_passengers.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    csv_data = [[parse_time(row[1]), row[5]] for row in spamreader if row[2] not in filter_terminals]

# csv = sc.textFile('lax_passengers.csv')
# rows = csv.flatMap(lambda x: x.split(','))
# rows = csv.flatMap(parse_vals)
rows = sc.parallelize(csv_data)

counts = rows \
    .map(lambda x: (x[0], int(x[1]))) \
    .reduceByKey(add)

# output = counts.collect()
# for v in output:
#     print '%s, %s' % (v[0], v[1])
for v in counts.collect():
    if v[1] > 5000000:
        print '%s, %s' % (v[0], v[1])
