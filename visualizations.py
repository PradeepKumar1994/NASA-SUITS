# -*- coding: utf-8 -*-
"""
Created on Sat May 30 20:44:07 2020

@author: prade
"""


import plotly.express as px
import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import plotly.express as px


astro_data_1_hour = pd.read_json("D:/Practice/NASA SUITS/astro_data.json")
data_one_hour = astro_data_1_hour


astro_data_2_hour = pd.read_json("D:/Practice/NASA SUITS/astr0-02_00.json")
data_two_hour = astro_data_2_hour 


astro_data_3_hour = pd.read_json("D:/Practice/NASA SUITS/astro-03_00.json")
data_third_hour = astro_data_3_hour



astro_data_4_hour = pd.read_json("D:/Practice/NASA SUITS/astro-04_00.json")
data_four_hour = astro_data_4_hour


astro_data_4_14_hour = pd.read_json("D:/Practice/NASA SUITS/db-04_14_00.json")
data_four__14_hour = astro_data_4_14_hour






data = astro_data

class dataset:
    
    def __init__(self,data):
        
        self.data = data
        
    
    def data_cleaning(self):
        
        pass
    
    def data_presenting(self):
        
        pass
    
    
plt.plot(data_one_hour['batteryPercent'])
plt.plot(data_two_hour['batteryPercent'])

desc_data_1_hr = data_one_hour.describe()


desc_data_2_hr = data_two_hour.describe()


























import plotly.graph_objects as go

# Create random data with numpy
import numpy as np
np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=data_one_hour['heart_bpm'], y=data_one_hour['ox_primary'],
                    mode='lines',
                    name='lines'))
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers'))
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', name='markers'))

fig.show()




import matplotlib.pyplot as plt































