from distutils.log import debug
from tokenize import group
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#DAF5F1',
    'text':'#10473E'
}

df1 = pd.DataFrame({
    "City":["Tokyo","Delhi","Shanghai","Dhaka","Sao Paulo","Mexico City","Cairo","Beijing","Mumbai","Osaka","Chongqing","Karachi"],
    "Population(mil)":[37,32,28,22,22,22,21,21,20,19,16,16],
    "Country":["Japan","India","China","Bangladesh","Brazil","Mexico","Egypt","China","India","Japan","China","Pakistan"]
})

fig1 = px.bar(df1, x = 'City', y = 'Population(mil)', color = 'Country')

fig1.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
)

app.layout = html.Div(style = {'backgroundColor': colors['background']} ,children=[html.H1("12 Most Populous Cities in the World", style = {'textAlign':'center','color':colors['text']}),
                    html.Div('''Have a look whether you live in one of them!''', style = {'textAlign':'center','color':colors['text']}),
                    dcc.Graph(id = 'eg_graph', figure = fig1)])


if __name__ == '__main__':
    app.run_server(debug=True)