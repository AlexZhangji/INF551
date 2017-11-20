from operator import add

from pyspark import SparkContext


def parse_time(prev_time):
    # 01/01/2006 12:00:00 AM
    time = prev_time.split()[0]
    month, year = time.split('/')[0], time.split('/')[2]
    return '{}/{}'.format(month, year)


sc = SparkContext(appName="inf551")
csv = sc.textFile('lax_passengers.csv')
# rows = csv.flatMap(lambda x: x.split(','))
rows = csv.flatMap(lambda x: x.split(','))

filter_terminals = ['Imperial Terminal', 'Misc. Terminal']
filtered_rows = [[parse_time(row[1]), row[5]] for row in rows if row[2] not in filter_terminals]
spark_rows = sc.parallelize(filtered_rows)

counts = spark_rows \
    .map(lambda x: (x[0], x[1])) \
    .reduceByKey(add)

output = counts.collect()
for v in output:
    print '%s, %s' % (v[0], v[1])
