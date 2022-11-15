import pandas as pd
import argparse
import matplotlib.pyplot as plt
import numpy as np

filename1 = sys.argv[-2]
filename2 = sys.argv[-1]

url = "owid-covid-data-2020-monthly.csv"
df = pd.read_csv("owid-covid-data-2020-monthly.csv")

del df['month']

df_new = df.groupby('location').sum()

df_new.describe()

plt.scatter(df_new['new_cases'],df_new['case_fatality_rate'], color = 'maroon')

plt.ylabel("Case Fatality Rate")
plt.xlabel("Confirmed New Cases")
plt.title("Case Fatality Rate Vs New Cases")
plt.grid(True)
plt.legend()
ax = plt.axes()
ax.set_facecolor("lightcyan")
plt.savefig(filename1)
plt.show()

df_new['new_cases'] = np.log(df_new['new_cases'])

plt.scatter(df_new['new_cases'],df_new['case_fatality_rate'], color = 'maroon')

plt.ylabel("Case Fatality Rate")
plt.xlabel("Confirmed New Cases")
plt.title("Case Fatality Rate Vs New Cases")
plt.grid(True)
plt.legend()
ax = plt.axes()
ax.set_facecolor("lightcyan")
plt.savefig(filename2)
plt.show()

