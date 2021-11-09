import plotly.express as px
import pandas as pd
 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
from app import app #change this line
 
# Data Preprocessing
df = pd.read_csv('supermarket_sales - Sheet1.csv')
df.drop(['Invoice ID', 'Unit price', 'Tax 5%', 'Date', 'Time'], axis=1, inplace=True)
df_index = df['City'].unique()
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Supermarket Sales Statistics"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='selected_city',
                    options=[
                       {'label': city, 'value': city} for city in df_index
                    ],
                    value='Yangon',
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='first-graph'
                ),
                width=6,className="mb-3"
            ),
            dbc.Col(
                dcc.Graph(
                    id='second-graph'
                ),
                width=6,className="mb-3"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='third-graph'
                ),
                className="mb-3"
            ),
            dbc.Col(
                dcc.Graph(
                    id='fourth-graph'
                ),
                width=6,className="mb-3"
            )
        ])
    ])
])
 
@app.callback(
    Output('first-graph', 'figure'),
    Output('second-graph', 'figure'),
    Output('third-graph', 'figure'),
    Output('fourth-graph', 'figure'),
    Input('selected_city', 'value')
)
def city_sales(city):

    figure1 = px.pie(df[df['City'] == city].groupby(['Product line'])['Quantity'].sum().reset_index(), names= 'Product line', values='Quantity', 
    color = 'Product line', title=f'Sum of Quantity based on Product Type in {city} Branch')

    figure2 = px.pie(df[df['City'] == city].groupby(['Product line'])['Total'].sum().reset_index(), names= 'Product line',values='Total', 
    color = 'Product line', title=f'Total Income based on Product Type in {city} Branch')

    figure3 = px.pie(df[df['City'] == city].groupby(['Payment'])['Total'].sum().reset_index(), names= 'Payment',values='Total', 
    color = 'Payment', title=f'Total Income based on Payment Type in {city} Branch')

    figure4 = px.pie(df[df['City'] == city].groupby(['Customer type'])['Total'].sum().reset_index(), names= 'Customer type',values='Total', 
    color = 'Customer type', title=f'Total Income based on Member Type in {city} Branch')
    return [figure1, figure2, figure3, figure4]
 
# remove the main things