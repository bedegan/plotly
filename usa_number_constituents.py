#!/usr/bin/env python
# coding: utf-8

# In[15]:


import plotly
plotly.__version__


# In[16]:


import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd


# In[17]:


df = pd.read_csv(r'C:\Users\Brenna\Desktop\usa_capstone.csv')

for col in df.columns:
    df[col] = df[col].astype(str)

scl = [
    [0.0, 'rgb(242,240,247)'],
    [0.2, 'rgb(218,218,235)'],
    [0.4, 'rgb(188,189,220)'],
    [0.6, 'rgb(158,154,200)'],
    [0.8, 'rgb(117,107,177)'],
    [1.0, 'rgb(84,39,143)']
]

data = [go.Choropleth(
    colorscale = scl,
    autocolorscale = False,
    locations = df['state'],
    z = df['number'],
    locationmode = 'USA-states',
    marker = go.choropleth.Marker(
        line = go.choropleth.marker.Line(
            color = 'rgb(255,255,255)',
            width = 2
        )),
    colorbar = go.choropleth.ColorBar(
        title = "# people")
)]

layout = go.Layout(
    title = go.layout.Title(
        text = 'Number of Constituents per State <br> rated over $100K'
    ),
    geo = go.layout.Geo(
        scope = 'usa',
        projection = go.layout.geo.Projection(type = 'albers usa'),
        showlakes = True,
        lakecolor = 'rgb(255, 255, 255)'),
)

fig = go.Figure(data = data, layout = layout)
py.iplot(fig)

