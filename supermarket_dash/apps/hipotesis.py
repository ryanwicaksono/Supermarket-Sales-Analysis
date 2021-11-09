import plotly.express as px
import pandas as pd
import numpy as np
from scipy import stats
 
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

#Define payment_product_line
payment_product_line = pd.crosstab(df['Payment'], df['Product line']).T
payment_product_line.reset_index(inplace=True)

#Define product_line_customer
product_line_customer = pd.crosstab(df['Customer type'], df['Product line']).T
product_line_customer.reset_index(inplace=True)

#Hypotesis Testing
#Inisiasi Variable yg_normal untuk menyimpan nilai City Yangon serta Pengunjung normal

normal_electronic = df[(df['Product line'] == 'Electronic accessories') & (df['Customer type'] == 'Normal')]

#Inisiasi Variable yg_normal untuk menyimpan nilai City Mandalay serta Pengunjung normal

normal_fashion = df[(df['Product line'] == 'Fashion accessories') & (df['Customer type'] == 'Normal')]

#Inisiasi untuk mengambil kolom total saja

normal_electronic_total = normal_electronic['Total']
normal_fashion_total = normal_fashion['Total']

#Independent test
t,p = stats.ttest_ind(normal_electronic_total, normal_fashion_total)
print ("t-statistic:" + str(t))
print("p-value:" + '%f' % p)


#Layout
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Hypotesis Testing"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P("Based on our supermarket sale dataset, we want to know about average of Total Income from Normal Customer who bought Electronic Accessories" + 
                " with average of Total Income from Normal Customer who bought Fashion Accessories. We can see a summary of data in graph shown below."),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='first-graph',
                    figure = px.bar(payment_product_line, x='Product line', y=['Cash', 'Credit card', 'Ewallet'])
                ),
                width=6,className="mb-3"
            ),
            dbc.Col(
                dcc.Graph(
                    id='second-graph',
                    figure = px.bar(product_line_customer, x='Product line', y=['Member', 'Normal'])
                ),
                width=6,className="mb-3"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H1("Set Hypotesis Testing"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P("H0 = Mean of Total Income from Normal Customer with Product line Electronic Accessories = Mean of Total Income form Normal Customer with Product line Fashion Accesories"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P("H1 = Mean of Total Income from Normal Customer with Product line Electronic Accessories != Mean of Total Income form Normal Customer with Product line Fashion Accesories"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H1("Testing"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P("Output : "),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P("t-stats = 0.571"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P("p-value = 0.56"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.P("From testing, we got p-value of 0.56, which means H0 failed to reject / H0 accepted because, p-values > 0.05. It can be concluded that Mean of Total Income from Normal Customer with Product line Electronic Accessories = Mean of Total Income form Normal Customer with Product line Fashion Accesories"),
                className="mb-2 mt-2"
            )
        ]),
    ])
    
])
 

# remove the main things