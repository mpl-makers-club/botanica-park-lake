import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

df = pd.read_csv("/home/pi/botanica-park-lake/BOM_rain.txt")
print(df)

fig = go.Figure()

fig.add_trace(go.Scatter(mode='markers',
                         x=df['day'],
                         y=df['rain'],
                         name="Rain",
                         marker=dict(
                             color="LightSkyBlue",
                             size=20,
                             line=dict(
                                 color="mediumPurple",
                                 width=2
                            )),
                         line_color='deepskyblue'))

fig.update_layout(
    title_text='BOM Melbourne 7-day Forecast',
    xaxis_title="Day",
    yaxis_title="Max rainfall (mm)",
    font=dict(
        size=26,
        color="RebeccaPurple"
        ),
    xaxis_rangeslider_visible=False)


plotly.offline.plot(fig,
                    filename="/home/pi/botanica-park-lake/BOM_rain.html",
                    auto_open=False)
print("BOM Melbourne Max rainfall forecast plotted")
