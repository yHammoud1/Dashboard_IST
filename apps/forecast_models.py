import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app


import pandas as pd
import  plotly.express as px

from sklearn.model_selection import train_test_split



df_model_dataset= pd.read_csv('Proj1_model_dataset.csv')
errors_table= pd.read_csv('errors_table.csv')
reg_table= pd.read_csv('reg_table.csv') 

errors_table= errors_table.round(3)

a_list = list(range(1, 200))
table_errors = dbc.Table.from_dataframe(errors_table,bordered= True, dark= True, hover = True,responsive= True )

df_model_dataset = df_model_dataset.drop(columns=['Date'])
X=df_model_dataset.values
Y=X[:,0] #output is power
X=X[:,[1,2,3,4,5,6]]
X_train, X_test, y_train, y_test = train_test_split(X,Y)




layout=html.Div(children=[
    html.Br(),
    html.Br(),
    html.H4('Testing Different Regression Models to Forecast Energy Consumption'),
    html.H5('The results of the errors produced by each model are presented in the below table'),

    html.Div(table_errors),
    html.Br(),
    html.Br(),
    html.H5('Choose among the regression models to view the predicted data'),
    dbc.FormGroup(
            [
                
                dcc.Dropdown(
                    id="regression-models",
                    options=[
                        {"label": i, "value": i } for i in errors_table.Method 
                    ],
                    value="Random Forest", ),
            ]),

    dcc.Graph(id='model-graphs'),
    ])



@app.callback(
     dash.dependencies.Output('model-graphs', 'figure'),
    [dash.dependencies.Input('regression-models', 'value')])
def update_figure(value):
    if ( value == 'Linear Regression'):
        return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_LR[1:200]], color='variable')
    
    elif ( value == 'Random Forest'): 
        return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_RF[1:200]], color='variable')
    
    
    elif ( value == 'Support Vector Machine'):       
        return px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_SVR[1:200]], color='variable')

    elif ( value == 'Regression Decision Tree'):
        return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_DT[1:200]], color='variable')
    elif ( value == 'Random Forest Uniformized Data'):
        return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_RFU[1:200]], color='variable')
    elif ( value == 'Gradient Boosting'):
       return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_GB[1:200]], color='variable')
    elif ( value == 'Extreme Gradient Boosting'):
        return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_XGB[1:200]], color='variable')
    elif ( value == 'Bootsrapping'):
        return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_BT[1:200]], color='variable')
    elif ( value == 'Neural Networks'):
        return  px.line(reg_table,x= a_list , y= [y_test[1:200],reg_table.y_pred_NN[1:200]], color='variable')

       