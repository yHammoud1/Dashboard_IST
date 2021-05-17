import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app


import pandas as pd
import  plotly.express as px


df_raw = pd.read_csv('Proj1_Clean.csv')

raw_columns = [col for col in df_raw.columns]
raw_columns.pop(0) 
raw_columns.pop(9)
raw_columns.pop(8)

def fix_tables(df):
    dff = df.Date
    df = df.drop(columns=['Date'])
    df = df.round(2)
    df.insert(0, 'Date', dff)
    return df

table1 = fix_tables(df_raw)

table = dbc.Table.from_dataframe(table1[1:6],bordered= True, dark= True, hover = True,responsive= True )


    


layout= html.Div(children=[
    html.Br(), 
    html.Br(), 
    html.H4('Plots of raw available data: Choose the parameter to be viewed'),
    dbc.FormGroup(
            [
                dcc.Dropdown(
                    id="dropdown-1",
                    options=[{"label": i, "value": i} for i in raw_columns
                    ],
                    value="Power_kW",
                ),
            ]
        ),

      html.Div(children=[
          html.Div(
        dcc.Graph(id='raw-data'), style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          html.Div(
          dcc.Graph(id='boxplt-raw') , style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          html.Br(), 
        html.H6('Sample table of raw data available'),
        html.Div(table)
                
        ]),
      ])


@app.callback(
    dash.dependencies.Output('raw-data', 'figure'),
    dash.dependencies.Output('boxplt-raw', 'figure'),
    [dash.dependencies.Input('dropdown-1', 'value')])
def prepare_raw_graphs(value):
     return {
        'data': [
            {'x': df_raw.Date, 'y': df_raw[value], 'type': 'scatter'},
        ],
        'layout': {
            'title': 'Raw data of ' + value 
        } }, px.box(df_raw, x=value)
 
    