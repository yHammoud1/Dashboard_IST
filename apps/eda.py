import dash
import dash_core_components as dcc
import dash_html_components as html

from app import app

import pandas as pd
import  plotly.express as px



df_zscore = pd.read_csv('Proj1_EDA_zscore.csv')
df_zscore_opp = pd.read_csv('Proj1_EDA_zscore_opp.csv')
df_IQR = pd.read_csv('Proj1_EDA_IQR.csv')
df_IQR_opp = pd.read_csv('Proj1_EDA_IQR_opp.csv')
df_EDA_final = pd.read_csv('Proj1_EDA_final.csv')
df_EDA_final_opp = pd.read_csv('Proj1_EDA_final_opp.csv')

layout=html.Div(children=[
      html.Br(), 
      html.Br(), 
      html.H4('Exploratory Data Analysis on Power Data'),
      dcc.Dropdown(
        id='dropdown-2',
          options=[
            {'label': 'Zscore Method', 'value': 1},
            {'label': 'IQR Method', 'value': 2},
            {'label': 'Final Outlier Removal', 'value': 3}
        ],
        value=3
    ),
     
    html.Div(children=[
          html.Div(
        dcc.Graph(id='EDA-data'), style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          html.Div(
          dcc.Graph(id='boxplt-EDA') , style={'width': '50%', 'display': 'inline-block', 'padding': '0 20'}
              ),
          ]),
    
    ])

@app.callback(
    dash.dependencies.Output('EDA-data', 'figure'),
    dash.dependencies.Output('boxplt-EDA', 'figure'),
    [dash.dependencies.Input('dropdown-2', 'value')])
def prepare_EDA_graphs(value):
    if (value ==1):
     return {
        'data': [
            {'x': df_zscore.Date, 'y': df_zscore['Power_kW'], 'type': 'scatter', 'name' : 'Correct Data'},
            {'x': df_zscore_opp.Date, 'y': df_zscore_opp['Power_kW'], 'type': 'scatter', 'name' : 'Outliers'},
        ],
        'layout': {
            'title': '          Outliers found in Power data'
        } }, px.box(df_zscore, x=df_zscore['Power_kW'], title = 'Boxplot after outliers removal')
 
    elif (value == 2):
        return {
        'data': [
            {'x': df_IQR.Date, 'y': df_IQR['Power_kW'], 'type': 'scatter', 'name' : 'Correct Data'},
            {'x': df_IQR_opp.Date, 'y': df_IQR_opp['Power_kW'], 'type': 'scatter', 'name' : 'Outliers'},
        ],
        'layout': {
            'title': '          Outliers found in Power data '
        } }, px.box(df_IQR, x=df_IQR['Power_kW'], title = 'Boxplot after outliers removal') 
    
    elif (value == 3):
        return {
        'data': [
            {'x': df_EDA_final.Date, 'y': df_EDA_final['Power_kW'], 'type': 'scatter', 'name' : 'Correct Data'},
            {'x': df_EDA_final_opp.Date, 'y': df_EDA_final_opp['Power_kW'], 'type': 'scatter', 'name' : 'Outliers'},
        ],
        'layout': {
            'title': '          Outliers to be finally removed Power data'
        } }, px.box(df_EDA_final, x=df_EDA_final['Power_kW'], title = 'Boxplot after outliers removal')
