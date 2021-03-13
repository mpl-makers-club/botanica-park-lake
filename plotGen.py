import pandas as pd
import plotly
import plotly.graph_objs as go
from plotly.graph_objs import Scatter, Layout

df = pd.read_csv("/home/pi/botanica-park-lake/data.txt")
print(df)

fig = go.Figure()

fig.add_trace(go.Scatter(x=df.date, y=df['count'], name="Count",
                         line_color='deepskyblue'))

fig.update_layout(title_text='Daily Litter Count',
                  xaxis_rangeslider_visible=False)


plotly.offline.plot(fig,
                    filename='/home/pi/botanica-park-lake/dataLitterPlot.html',
                    auto_open=False)
print("Litter data plotted")
