import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/', order=0)

green_text = {'color':'green'}
#image card
picture_card = dbc.Card(
    [
        dbc.CardImg(src="assets/portrait.jpeg", top=True),
        #dbc.CardBody(
            #html.P("This card has an image at the top", className="card-text")
        #),
    ],
    style={"width": "18rem"}, className='border rounded-lg',
)

def layout():
    return dbc.Row([

        # put image here
        dbc.Col([
            picture_card
        ], width={"size": 3}),

        dbc.Col([
            dcc.Markdown('### Raimi Azeez Babatunde', style={'textAlign': 'center'}),
            html.Hr(),
            html.P("Hi, I'm glad you found me.\n \n"
                 "Welcome to my world of data-driven wonders! I'm Azeez, your go-to wizard for turning raw data "
                 "into game-changing insights. With a passion for Python, data analysis, visualization, "
                 "and machine learning, I'm on a mission to unravel the untold stories hidden in data.",
                 style={'textAlign': 'left'}),

            html.P("From crunching numbers to crafting visually stunning dashboards, I thrive on transforming "
                 "complexity into clarity. My insatiable curiosity and love for problem-solving keep me at "
                 "the forefront of cutting-edge technologies and trends",
                   style={'textAlign': 'left'}),

            html.P("When I'm not geeking out on data, you can find me exploring the fascinating realms of "
                 "Finance, or in the field flexing my photography skills.\n"
                 "Ready to embark on a data-driven adventure? Let's innovate together!",
                   style={'textAlign': 'left'}),

        ], width={'size':6}, className='flex-wrap')
], justify='center', className='p-3')