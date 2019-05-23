import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

input_string = input("Enter lists of data separated by comma and space")
data_list = input_string.split("], [")

for z in data_list:
    print (z)



#if i data is not organized by age, use sorting algorithm to sort by age
men_count = 0
women_count = 0
for x in data_list:
    if data_list[x][1] == "1":
        womens_list[women_count] = data_list[x][2]
    else:
        mens_list[men_count] = data_list[x][2]

for i in womens_list:
    print(i)

layout = go.Layout(yaxis=go.layout.YAxis(range=[0,150], title='Age'),
                   xaxis=go.layout.XAxis(
                       range=[-100, 100],
                       tickvals=[-100, -70, -30, 0, 30, 70, 100],
                       ticktext=[100, 70, 30, 0, 30, 70, 100],
                       title='Percent of Population'),
                   barmode='overlay',
                   bargap=0.1)
