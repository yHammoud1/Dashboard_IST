import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app

import pandas as pd
import plotly.graph_objs as go
from sklearn.cluster import KMeans



df_kmeans_1= pd.read_csv('Proj1_Cluster_kmeans1.csv')
df_kmeans_2= pd.read_csv('Proj1_Cluster_kmeans2.csv')
df_load_curve= pd.read_csv('Proj1_Cluster_loadcurve.csv')

                
controls = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("X variable"),
                dcc.Dropdown(
                    id="x-variable",
                    options=[
                        {"label": 'Power', "value":'Power_kW' },
                        {"label": 'Hour', "value":'Hour' }, 
                        {"label": 'Week Day', "value":'Week Day' } 
                    ],
                    value="Power_kW",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Y variable"),
                dcc.Dropdown(
                    id="y-variable",
                    options=[
                        {"label": 'Temperature', "value": 'temp_C' },
                        {"label": 'Power', "value":'Power_kW' }
                    ],
                    value="temp_C",
                ),
            ]
        ),
        
    ],
    body=True,
)

controls1 = dbc.Card(
    [
        dbc.FormGroup(
            [
                dbc.Label("X variable"),
                dcc.Dropdown(
                    id="x-variable1",
                    options=[
                        {"label": 'Power', "value":'Power_kW' },
                    ],
                    value="Power_kW",
                ),
            ]
        ),
        dbc.FormGroup(
            [
                dbc.Label("Y variable"),
                dcc.Dropdown(
                    id="y-variable1",
                    options=[
                        {"label": 'Humidity', "value": 'HR' },
                        {"label": 'Wind Speed', "value":'windSpeed_m/s' },
                        {"label": 'Solar Radiation', "value":'solarRad_W/m2' },
                    ],
                    value="HR",
                ),
            ]
        ),
        
    ],
    body=True,
) 



layout=html.Div(children=[
    html.Br(), 
    html.Br(), 
    html.H4('Clustering of Data Using Kmeans and Clustered Load Curve Results'),
    dcc.Tabs(id='tabs-1', value='tab-1', children=[
         dcc.Tab(label='Kmeans', value='tab-1'),
         dcc.Tab(label='Indentifying Daily Patterns', value='tab-2'),
     ]),
    
    html.Div(id='tabs-content'), 
    ])


@app.callback(
    dash.dependencies.Output('tabs-content', 'children'),
    [dash.dependencies.Input('tabs-1', 'value')])
def show_content(value):
    
    if (value == 'tab-1'):
        return html.Div([
       html.H5('Clustering using Kmeans: trials with sets of different parameters'),
       html.H6('Optimal number of clusters was found to be 3'),
        html.Br(), 
        html.H6('Trial 1: Power, Temperature, Weekday and Hour'),
       
        dbc.Row(
            [
                dbc.Col(controls, md=4),
                dbc.Col(dcc.Graph(id="cluster-graph"), md=8),
            ],
            align="center",
                ),
        html.H6('Trial 2: Power, Humidity, Wind speed and Solar radiation'),
            
        dbc.Row(
            [
                dbc.Col(controls1, md=4),
                dbc.Col(dcc.Graph(id="cluster-graph2"), md=8),
            ],
            align="center",
                ),
        ])
    
            
    elif (value == 'tab-2'):
        return  html.Div([
            html.H6('Power load curve with 3 clusters'),
            
           html.Img(style={'display': 'block','margin-left': 'auto','margin-right': 'auto'}, src='assets\loadcurve.png')

            ])
    
    
@app.callback(
    dash.dependencies.Output('cluster-graph', 'figure'),
    [dash.dependencies.Input('x-variable', 'value'),
    dash.dependencies.Input('y-variable', 'value')])
def make_graph(x, y):
    km = KMeans(max(3, 1))
    df = df_kmeans_1.loc[:, [x, y]]
    km.fit(df.values)
    df["cluster"] = km.labels_

    data = [
        go.Scatter(
            x=df.loc[df.cluster == c, x],
            y=df.loc[df.cluster == c, y],
            mode="markers",
            marker={"size": 8},
            name="Cluster {}".format(c),
        )
        for c in range(3)
    ]
    layout = {"xaxis": {"title": x}, "yaxis": {"title": y}}

    return go.Figure(data=data, layout=layout)
  
@app.callback(
    dash.dependencies.Output('cluster-graph2', 'figure'),
    [dash.dependencies.Input('x-variable1', 'value'),
    dash.dependencies.Input('y-variable1', 'value')])
def make_graph1(x, y):
    km = KMeans(max(3, 1))
    df = df_kmeans_2.loc[:, [x, y]]
    km.fit(df.values)
    df["cluster"] = km.labels_

    data = [
        go.Scatter(
            x=df.loc[df.cluster == c, x],
            y=df.loc[df.cluster == c, y],
            mode="markers",
            marker={"size": 8},
            name="Cluster {}".format(c),
        )
        for c in range(3)
    ]
    layout = {"xaxis": {"title": x}, "yaxis": {"title": y}}

    return go.Figure(data=data, layout=layout)