import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, callback
from dash.dependencies import Input, Output, State

from .def_symbols_tv import get_symbol_names, TIMEFRAMES, TIMEFRAME_DICT
from .side_bar import sidebar
from .vhf_chart_tv_white import price_chart

dash.register_page(__name__,  order=3, name='Live Chart')

symbol_dropdown = html.Div([
    html.P('Symbol:'),
    dcc.Dropdown(
        id='symbol-dropdown',
        options=[{'label': symbol, 'value': symbol} for symbol in get_symbol_names()],
        value='EURUSD',
    )
])

timeframe_dropdown = html.Div([
    html.P('Timeframe:'),
    dcc.Dropdown(
        id='timeframe-dropdown',
        options=[{'label': timeframe, 'value': timeframe} for timeframe in TIMEFRAMES],
        value='M5',
    )
])

slow_ema_input = html.Div([
    html.P('Slow EMA'),
    dbc.Input(id='slow_ema', type='number', value='200')
])

fast_ema_input = html.Div([
    html.P('Fast EMA'),
    dbc.Input(id='fast_ema', type='number', value='55')
])
def layout():
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                    sidebar()
                    ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            # heading title
            dbc.Col([
                html.H2('FOREX Live Chart Window', style={'textAlign': 'center'}, className='text-center p4'),
                #html.H1('TRADING DASHBOARD', className='text-center', style={"color": "#FFFFFF"}),
                html.P('This is a Live chart window which shows the live price of different financial assets on '
                       'different time frames including two different Estimated Moving Averages (EMA). '
                       'The live chart was created using data source from Tradingview.'
                       , style={'textAlign': 'left'}),
                html.Hr(),

                dbc.Row([
                    dbc.Col([
                        symbol_dropdown,
                    ], xs=2, sm=2, md=2, lg=2, xl=2, className='p-3', align='center'),
                    dbc.Col([
                        timeframe_dropdown,
                    ], xs=2, sm=2, md=2, lg=2, xl=2, className='p-3', align='center'),

                    dbc.Col([
                        slow_ema_input,
                    ], xs=2, sm=2, md=2, lg=2, xl=2, className='p-3', align='center'),

                    dbc.Col([
                        fast_ema_input,
                    ], xs=2, sm=2, md=2, lg=2, xl=2, className='p-3', align='center'),

                ], className='align-items-end', justify='center'),
                html.Br(),
                dbc.Row([
                    dbc.Col([
                        html.Div(id='page-content')
                    ], xs=10, sm=10, md=12, lg=12, xl=12, xxl=12, className='p-6', align='center')

                ], justify='right', style={"height": "60%"}, className='p-6')

            ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10, align='center'), #xs=8, sm=8, md=10, lg=10, xl=10,
        ], justify='center', style={"height": "20%"}),  # , "background-color": "cyan"

        dcc.Interval(id='update', interval=2000),

    ], fluid=True, class_name='g-0 p-4',
        style={"height": "99vh", 'background-size': '100%'})

@callback(
    Output('page-content', 'children'),
    Input('update', 'n_intervals'),
    State('symbol-dropdown', 'value'), #State('num-bar-input', 'value'),
    State('timeframe-dropdown', 'value'),
    State('slow_ema', 'value'), State('fast_ema', 'value')
)
def update_ohlc_chart(interval, symbol, timeframe, ema_slow, ema_fast): #, symbol, num_bars, timeframe, ema_slow, ema_fast):
    timeframe_str = timeframe
    timeframe = TIMEFRAME_DICT[timeframe]
    #num_bars = int(num_bars)
    ema_slow = int(ema_slow)
    ema_fast = int(ema_fast)

    fig = price_chart(symbol, timeframe, ema_slow, ema_fast)

    return [
        html.H5(id='chart-details', children= f'{symbol} {timeframe_str}', style={'textAlign': 'left'}), #"Trading View"
        dcc.Graph(figure=fig, config={'displayModeBar': False}),
        #dcc.Graph(figure=fig2, config={'displayModeBar': False})
        ]