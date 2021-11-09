import dash_html_components as html
import dash_bootstrap_components as dbc
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Supermarket Sales Dashboard",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='This is Supermarket Sales Dashboard made by Ryan Wicaksono.'),
                className="mb-4")
        ]),
 
        dbc.Row([
            dbc.Col(
                html.H5(children='It have two main pages: Statistics and Hypotesis. Feel free to explore it'),
                className="mb-5")
        ]),
 
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Statistic Page',
                        className="text-center"),
                        dbc.Button("Statistics",
                        href="/apps/visualisasi_data",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Hypotesis Page',
                        className="text-center"),
                        dbc.Button("Hypotesis",
                        href="/apps/hipotesis",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
        ], className="mb-5"),
    ])
 
])