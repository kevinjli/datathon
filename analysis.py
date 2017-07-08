import matplotlib.pyplot as plt
import numpy
import pandas as pd

get_ipython().magic('matplotlib inline')

econ = pd.read_csv('econ_industry.csv')
fuel = pd.read_csv('fossil_fuel_consumption.csv')
oil = pd.read_csv('oil_prices.csv')
photo = pd.read_csv('photovoltaic.csv')
radiation = pd.read_csv('solar_radiation.csv')
demographics = pd.read_csv('demographics.csv', encoding='mac_roman')

photo['date_installed'] = pd.to_datetime(photo['date_installed'])

state = photo[photo['state'] == 'NJ']

group = state[state['install_type'] == 'Residential'].sort('date_installed')
group['cumsum'] = group['size_kw'].cumsum()

plt.plot(group['date_installed'],group['cumsum'])

group = group[group['date_installed'] > '2001-1-1']
group['cumsum'] = group['size_kw'].cumsum()

plt.plot(group['date_installed'],group['cumsum'])
plt.title('size_kw over time CA Residential')
plt.plot(group['date_installed'],group['cost_per_watt'])

def movingaverage(interval, window_size):
    window = numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')

x_avg = movingaverage(group['cost_per_watt'], 100)
plt.plot(group['date_installed'],x_avg)

x_avg = movingaverage(group['cost_per_watt'], 20)
plt.plot(group['date_installed'],x_avg)

def two_scales(ax1, time, data1, data2, c1, c2):
    ax2 = ax1.twinx()

    ax1.plot(time, data1, color=c1)
    ax1.set_ylabel('cumulative size of solar panel installer (kilowatt)')

    ax2.plot(time, data2, color=c2)
    ax2.set_ylabel('cost per watt')

    return ax1, ax2

s1 = group['cumsum']
s2 = movingaverage(group['cost_per_watt'], 30)

fig, ax = plt.subplots(figsize=(10, 8))

ax1, ax2 = two_scales(ax, group['date_installed'], s1, s2, 'r', 'b')

def color_y_axis(ax, color):
    for t in ax.get_yticklabels():
        t.set_color(color)

    return None

color_y_axis(ax1, 'r')
color_y_axis(ax2, 'b')

plt.title('NJ Residential')
plt.show()
