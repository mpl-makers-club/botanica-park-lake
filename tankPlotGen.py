import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

df = pd.read_csv("/home/pi/botanica-park-lake/tank_data.txt")
print(df)

fig = go.Figure()

fig.add_trace(go.Scatter(mode='markers',
                         x=df.date,
                         y=df['level'],
                         name="Level",
                         marker=dict(
                             color="LightSkyBlue",
                             size=20,
                             line=dict(
                                 color="mediumPurple",
                                 width=2
                            )),
                         line_color='deepskyblue'))

fig.update_layout(
    title_text='Rainwater Tank Water Level',
    xaxis_title="Time",
    yaxis_title="Tank Level (m)",
    font=dict(
        size=26,
        color="RebeccaPurple"
        ),
    xaxis_rangeslider_visible=False)


plotly.offline.plot(fig,
                    filename="/home/pi/botanica-park-lake/tankLevelPlot.html",
                    auto_open=False)
print("tank level plotted")
