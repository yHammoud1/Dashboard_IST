
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd



df_feature_eng= pd.read_csv('Proj1_final_dataset.csv')
df_model_dataset= pd.read_csv('Proj1_model_dataset.csv')


def fix_tables(df):
    dff = df.Date
    df = df.drop(columns=['Date'])
    df = df.round(2)
    df.insert(0, 'Date', dff)
    return df

table2 = fix_tables(df_feature_eng)
table3 = fix_tables(df_model_dataset)

table = dbc.Table.from_dataframe(table2[1:6],bordered= True, dark= True, hover = True,responsive= True )
table1 = dbc.Table.from_dataframe(table3[1:6],bordered= True, dark= True, hover = True,responsive= True )


layout=html.Div(children=[
     html.Br(), 
      html.Br(), 
      html.H4('Feature Engineering/Extraction'),
      html.H6('New features were engineered to optimize the modeling using the available data: Log(Temp), Holiday*Weekday, Heating degree.hour and Power-1'),
      html.Div(table),
       html.Br(), 
       html.Br(),
      
      html.H5('Final features selected to perform the modelling are presented in the following table'),
      html.H6('After applying Filter, Wrapper and Ensemble methods, the most relevant features selected were: Power-1, hour, temperature, Solar radiation, holiday and weekday'),
      html.Div(table1),

])

