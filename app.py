# Import required libraries
import os
from random import randint

import plotly.plotly as py
from plotly.graph_objs import *

import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html


# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)

app.layout = html.Div([

    dbc.Row([html.Br(), html.Br(),
             dbc.Col(lg=1),
             dbc.Col([html.Img(src=app.get_asset_url('saco_logo.png'))], lg=1),
             dbc.Col([html.Br(), html.Br(), html.Div([html.P("Hello Worlds")],
                                                     style={'textAlign': "center", 'font-size': '300%',
                                                            'font-family': 'Roboto Condensed',
                                                            'font-weight': 'bold'})]),
             dbc.Col([html.Img(src=app.get_asset_url('saco_logo.png'))], lg=1),
             dbc.Col(lg=1)
             ]),


    dbc.Row([html.Br(), html.Br(),
            dbc.Col(lg=1),
            dbc.Col(dcc.Dropdown(id = "drop",
                                 placeholder= "Select Item",
                               #  value= ,
                                 options = [{'label':u, 'value': u}  for u in uniq_sex]), lg = 3)

            ]),

    dbc.Row([

        dbc.Col([html.Br(),
                 html.Div([html.Br(), html.Label('By Gender'),
                           dcc.Graph(id='graph', config={'displayModeBar': False})
                           ], style={'border': '2px solid gray', 'border-radius': '15px', 'font-size': '140%',
                                     # 'font-family': 'Roboto Condensed',
                                     'font-weight': 'bold',
                                     'textAlign': 'center'})], lg=7)
])
])


@app.callback(Output("graph", "figure"),
    [Input('drop', 'value')])

def update_graph(gender):
    df2 = df[df['Sex']== gender]

    outcome = go.Pie(
        labels = ["A", "B"], values = [20, 80] ,  marker=dict(colors=['#da202a', '#2a2a2d', '#c1c6c8']
                                                            , line=dict(color='#FFF', width=2)),
                                                            domain={'x': [0.0, .7], 'y': [0.0, 1]}
                                                            , showlegend=True, name='Test Pie', textinfo= 'label+value')

    layout = go.Layout(height=700,
                       width=800,
                       autosize=True,
                       legend={"x": 0, "y": 0}

                       )

    fig = go.Figure(data = outcome , layout = layout)


    return fig.to_dict()


# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
