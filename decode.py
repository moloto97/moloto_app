from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import columns as cols

# # Get all columns to display
col1 = cols.col1()
col2 = cols.col2()
col3 = cols.col3()


dash_style = 'd'
bootstrap = 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css'

ext_sheets = [{'href' : dash_style}, bootstrap]


app = Dash(external_stylesheets=ext_sheets)

# app = Dash(__name__)
 
app.layout = html.Div(
    id='container',
    className='col-md-12',
    style={'text-align': 'center'},
    children=[
        
        html.Div(id='logo-filters', className='col-md-12',
                # style={'text-align': 'center'},
                children=[
                    html.Div(#className='col-md-12', 
                             id='logo',
                            # style={'width': '50%'},
                            children=[
                                html.Img(src='/static/images/app_logo.png', id='agincourt-logo',style={'width': '100%', 'height':'70px'})
                            ])
                ])
    ,html.H1('MITS Decoder (Determining Causes of Deaths)', id='title', style={'text-decoration': 'underline', 'background-color': '#f3f5fe'}),
    html.Div(
    style={'margin-left': 'auto', 'width': '90%'},
    className='container',
    children=[
        html.Div(
            className='row',
            children=[
                # html.Div(className='col text-primary', children=["Col 1"]),
                # html.Div(className='col', children=["Col 2"]),
                col1,
                col2,
                col3
                
            ]
            ,style={'text-align': 'center'},
        ),
    ]
    # ,fluid=True,
    )
    ]
    

)



if __name__ == '__main__':
    app.run_server(debug=False)
    # app.run_server(debug=True, use_reloader=False)

