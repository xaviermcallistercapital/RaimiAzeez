import dash
import dash_bootstrap_components as dbc
from dash import html

from pages.side_bar import sidebar

dash.register_page(__name__, name='Time Series')

def layout():
    return html.Div([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H3('beautiful app 2'),
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
])