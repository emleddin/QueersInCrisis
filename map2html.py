"""
This code was tested using Anaconda 3.7

Render the plotly figure as an HTML section using a CDN link for the required js.

The original code was pulled from plotly: https://plotly.com/python/scatter-plots-on-maps/
"""

import plotly.graph_objects as go
import pandas as pd

## Add path to generate figure
CR_inset_path = "docs/CR-plotly-map-test.html"

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_february_us_airport_traffic.csv')
df['text'] = df['airport'] + '' + df['city'] + ', ' + df['state'] + '' + 'Arrivals: ' + df['cnt'].astype(str)

fig = go.Figure(data=go.Scattergeo(
        lon = df['long'],
        lat = df['lat'],
        text = df['text'],
        mode = 'markers',
        marker_color = df['cnt'],
        ))

fig.update_layout(
        title = 'Most trafficked US airports<br>(Hover for airport names)',
        geo_scope='usa',
    )

## Write a valid <div> section to embed in an HTML doc
## Use a CDN instead of embedding the js into the HTML
## Source: https://plotly.com/python/interactive-html-export/
fig.write_html(CR_inset_path, include_plotlyjs="cdn")
