import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

df = pd.read_csv("/home/pi/botanica-park-lake/soil_data.txt")
print(df)

fig = go.Figure()

fig.add_trace(go.Scatter(x=df.date, y=df['soil'], name="Soil",
                         line_color='deepskyblue'))

fig.update_layout(title_text='Botanica Park Soil Moisture Sensor',
                  xaxis_rangeslider_visible=False)


plotly.offline.plot(fig,
                    filename="/home/pi/botanica-park-lake/soilMoistPlot.html",
                    auto_open=False)
print("soil moisture plotted")
