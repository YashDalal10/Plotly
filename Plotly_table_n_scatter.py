from distutils.log import debug
from tokenize import group
from turtle import ht
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

df = pd.read_csv('health_df.csv')

def generate_table(dataframe, max_rows = 10):
    return html.Table([
        html.Thead(html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])

fig = px.scatter(df, x = "FLit11", y = "IMR_2011", size = "Pop_2011", color = "State", hover_name = "District", size_max = 30)

app = Dash(__name__)

app.layout = html.Div([
    html.H4(children = 'Dataframe'),
    generate_table(df),
    dcc.Graph(id = 'life-exp-vs-gdp', figure = fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
