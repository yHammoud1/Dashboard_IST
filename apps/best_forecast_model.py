
import dash_html_components as html
import dash_bootstrap_components as dbc


import pandas as pd


df_model_dataset= pd.read_csv('Proj1_model_dataset.csv')
RF_table= pd.read_csv('RF_table.csv')
RF_table= RF_table.round(3)
table = dbc.Table.from_dataframe(RF_table,bordered= True, dark= True, hover = True,responsive= True )


layout=html.Div(children=[
    html.Br(),
    html.Br(),
    html.H4('The best forecasting model chosen according to the results of each regression was found to be Random Forest'),
    html.Br(),
    html.H6('Several trials were done by chnaging some of the parameters of the model in order to optimize the forecasted data'),

    html.H6('Trial 1: min_samples_leaf= 2, n_estimators= 100'),
    html.Br(),
    html.H6('Trial 2: min_samples_leaf= 3, n_estimators= 150, min_samples_split= 10'),
    html.H6('Trial 3: min_samples_leaf= 3, n_estimators= 150, min_samples_split= 10, max depth= 40'),
    html.Div(table),
    ])