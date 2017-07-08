
# coding: utf-8

# In[1]:

#import libraries

import pandas as pd
import numpy as np
import pylab as pl
import seaborn as sns
import random
import matplotlib.pyplot as plt
import matplotlib as mpl
import scipy.stats as stats

from math import sqrt
from scipy.stats.stats import pearsonr
from scipy.stats import linregress
from scipy.stats import ttest_1samp

get_ipython().magic('matplotlib inline')


# In[2]:

econ = pd.read_csv('econ_industry.csv')
fuel = pd.read_csv('fossil_fuel_consumption.csv')
oil = pd.read_csv('oil_prices.csv')
photo = pd.read_csv('photovoltaic.csv')
radiation = pd.read_csv('solar_radiation.csv')
demographics = pd.read_csv('demographics.csv', encoding='mac_roman')


# In[19]:

photo['date_installed'] = pd.to_datetime(photo['date_installed'])


# In[84]:

state = photo[photo['state'] == 'NJ']


# In[135]:

group = state[state['install_type'] == 'Residential']


# In[136]:

group = group.sort('date_installed')


# In[137]:

group.head()


# In[138]:

group['cumsum'] = group['size_kw'].cumsum()


# In[139]:

plt.plot(group['date_installed'],group['cumsum'])


# In[140]:

type(group['date_installed'].iloc[0])


# In[141]:

group = group[group['date_installed'] > '2001-1-1']


# In[142]:

group.shape


# In[143]:

group['cumsum'] = group['size_kw'].cumsum()


# In[144]:

plt.plot(group['date_installed'],group['cumsum'])
plt.title('size_kw over time CA Residential')


# In[145]:

plt.plot(group['date_installed'],group['cost_per_watt'])


# In[146]:

import numpy
def movingaverage(interval, window_size):
    window = numpy.ones(int(window_size))/float(window_size)
    return numpy.convolve(interval, window, 'same')
x_avg = movingaverage(group['cost_per_watt'], 100)
plt.plot(group['date_installed'],x_avg)


# In[147]:


x_avg = movingaverage(group['cost_per_watt'], 20)
plt.plot(group['date_installed'],x_avg)


# In[150]:

def two_scales(ax1, time, data1, data2, c1, c2):
    """

    Parameters
    ----------
    ax : axis
        Axis to put two scales on

    time : array-like
        x-axis values for both datasets

    data1: array-like
        Data for left hand scale

    data2 : array-like
        Data for right hand scale

    c1 : color
        Color for line 1

    c2 : color
        Color for line 2

    Returns
    -------
    ax : axis
        Original axis
    ax2 : axis
        New twin axis
    """
    ax2 = ax1.twinx()

    ax1.plot(time, data1, color=c1)
    ax1.set_ylabel('cumulative size of solar panel installer (kilowatt)')

    ax2.plot(time, data2, color=c2)
    ax2.set_ylabel('cost per watt')
    return ax1, ax2
s1 = group['cumsum']
s2 = movingaverage(group['cost_per_watt'], 30)

# Create axes
fig, ax = plt.subplots(figsize=(10, 8))
ax1, ax2 = two_scales(ax, group['date_installed'], s1, s2, 'r', 'b')

# Change color of each axis
def color_y_axis(ax, color):
    """Color your axes."""
    for t in ax.get_yticklabels():
        t.set_color(color)
    return None
color_y_axis(ax1, 'r')
color_y_axis(ax2, 'b')
plt.title('NJ Residential')
plt.show()


# In[ ]:



