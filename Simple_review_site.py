from dash import Dash, html, dcc

colors = {
    'background': '#DAF5F1',
    'text':'#10473E'
}

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children = [
        html.H1('Select the product from the menu for rating'),
        html.H3('Select the product for review'),
        # html.Label('Dropdown'),
        # dcc.Dropdown(['Computer Science','Artificial Intelligence','Electronics','Economics','Management'], 'Artificial Intelligence'),
        # html.Br(),
        html.Label('Multi-Select Dropdown'),
        dcc.Dropdown(['Shoes','T Shirts','Jackets','Caps','Trousers'], multi = True),
        html.Br(),
        html.H3('Like the product?'),
        html.Label("Radio Items"),
        dcc.RadioItems(['Yes','No','Undecided']),
        html.H3('Select the quality of the product'),
        html.Label('Checkboxes'),
        dcc.Checklist(['Durable','Cheap and Good','Not worth the money','Bad quality','Satisfactory']),
        html.Br(),
        html.H3('Type your review here'),
        html.Label('Text Input'),
        dcc.Input(value = 'Please type here', type = 'text'),
        html.H3('Rate the product'),
        html.Br(),
        html.Label('Slider'),
        dcc.Slider(min = 0, max = 5, marks = {i: f'label{i}' if i==1 else str(i) for i in range(1,5)}, value = 3),
        ], style = {'padding': 10, 'flex': 1, 'textAlign':'center','color':colors['text']})
    ], style = {'display': 'flex', 'flex-direction':'row', 'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)
