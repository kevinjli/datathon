import matplotlib.pyplot as plt
import pandas as pd

solar_radiation = pd.read_csv('solar_radiation.csv')

ca_solar = solar_radiation[solar_radiation['state'] == 'CA '].groupby(['year', 'month', 'day']).max()['ghi']
nj_solar = solar_radiation[solar_radiation['state'] == 'NJ '].groupby(['year', 'month', 'day']).max()['ghi']
nd_solar = solar_radiation[solar_radiation['state'] == 'ND '].groupby(['year', 'month', 'day']).max()['ghi']

plt.plot(ca_solar.rolling(window=14).mean().tolist()[-365*3:])
plt.plot(nj_solar.rolling(window=14).mean().tolist()[-365*3:])
plt.plot(nd_solar.rolling(window=14).mean().tolist()[-365*3:])
plt.show()
