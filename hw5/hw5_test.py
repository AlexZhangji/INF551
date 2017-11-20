import pandas as pd


def parse_time(prev_time):
    # 01/01/2006 12:00:00 AM
    time = prev_time.split()[0]
    month, year = time.split('/')[0], time.split('/')[2]
    return '{}/{}'.format(month, year)


df = pd.read_csv('lax_passengers_header.csv')
filter_terminals = ['Imperial Terminal', 'Misc. Terminal']
df_filtered = df[~df.Terminal.isin(filter_terminals)]
df_filtered['ReportPeriod'] = df_filtered['ReportPeriod'].apply(parse_time)
df_grouped = df_filtered.groupby(['ReportPeriod'])['Passenger_Count'].agg(['sum'])
df_grouped = df_grouped.query('sum > 5000000')

print df_grouped
# for pair in df_grouped:
#     print pair
