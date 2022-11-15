import pandas as pd
import argparse
import sys

url = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
df = pd.read_csv(url)

df_new = df.loc[:,['location','date','total_cases','new_cases','total_deaths','new_deaths']]
df_2020 = df_new.loc[df_new['date'] < '2021']

df_2020['month'] = pd.DatetimeIndex(df_2020['date']).month
del df_2020['date']

new_group = df_2020.groupby(['location','month']).sum()

new_group['case_fatality_rate'] = new_group['total_deaths']/new_group['total_cases']

new_group = new_group[['case_fatality_rate','total_cases','new_cases','total_deaths','new_deaths']]

print(new_group.head())

filename = sys.argv[-1]

new_group.to_csv(filename)