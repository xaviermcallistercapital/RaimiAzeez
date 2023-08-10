#import
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, order=3)

#interest buttons
interests_buttons = html.Div(
    [
        dbc.Button("Finance", outline=True, color="primary", className="me-1"),
        dbc.Button("Analytics", outline=True, color="primary", className="me-1"),
        dbc.Button("Business", outline=True, color="primary", className="me-1"),
        dbc.Button("Technology", outline=True, color="primary", className="me-1"),
        dbc.Button("Algorithmic Trading", outline=True, color="primary", className="me-1"),
        ]
)

# resume sample template from https://zety.com/
layout = html.Div([
    dbc.Row([

        #Biodata
        dbc.Col([
            dcc.Markdown('# Raimi Azeez Babatunde', style={'textAlign':'center'}),
            dcc.Markdown('#### Data Scientist', style={'textAlign':'center'}),
            html.Hr(),
            # dcc.Markdown('#### Data Scientist',
            #              style={'textAlign':'center'})
            dcc.Markdown(" I am a Data Scientist with vast and efficient knowledge in using \n"
                            "python, data analysis, visualization,  and machine learning models & techniques to deliver "
                         "insights and implement action-oriented solutions to business problems. My goal is to work in "
                         "an environment where my potential and capabilities will be developed and utilized to attain "
                         " the organization's goals and make a real-life impact.",
                         #' \n',
                         style={'textAlign': 'left', 'white-space': 'pre'},
                         className='flex-wrap'),
            html.Hr(),
            #email and #phone
            dbc.Row([
                dbc.Col([
                    html.I(className="fa-solid fa-envelope"),  # <i class="fa-solid fa-envelope"></i>
                    dcc.Markdown('###### &ensp; raimiazeez26@gmail.com',
                        style={'textAlign':'center'}),
                ], width={"size": 4}, className= 'd-inline-flex'),

                dbc.Col([
                    html.I(className="fa-solid fa-phone"),  # <i class="fa-solid fa-envelope"></i>
                    dcc.Markdown('###### &ensp; +2348025831825',
                        style={'textAlign': 'center'}),
                ], width={"size": 3}, className= 'd-inline-flex'),

                ], justify="center", className= 'pt-1'),

            # social media
            dbc.Row([
                dbc.Col([
                    html.I(className="fa-brands fa-github p-1"), #<i class="fa-brands fa-github"></i>
                    html.A('GitHub  ', href='https://github.com/raimiazeez26', target="_blank",
                           style={'textAlign': 'center'})
                ], width={"size": 2}, className='d-inline-flex'),

                dbc.Col([
                    html.I(className="fa-brands fa-linkedin p-1"),
                    html.A('LinkedIn  ', href='https://www.linkedin.com/in/raimi-azeez/', target="_blank",
                                style={'textAlign':'left'})
                ], width={"size": 2}, className='d-inline-flex'),

                dbc.Col([
                    html.I(className="fa-brands fa-medium p-1"),
                    html.A('Medium  ', href='https://medium.com/@raimiazeez26', target="_blank",
                           style={'textAlign': 'left'})
                ], width={"size": 2}, className='d-inline-flex'),

                dbc.Col([
                    html.I(className="fa-brands fa-kaggle p-1"), #<i class="fa-brands fa-kaggle"></i>
                    html.A('Kaggle  ', href='https://www.kaggle.com/raimiazeezbabatunde', target="_blank",
                           style={'textAlign': 'left'})
                ], width={"size": 2}, className='d-inline-flex'),
            ], justify="center", style={'align':'center'}),

        ], width={"size": 8}, className= 'p-3'), #, "offset": 4
        ], justify="center"),

    #Skills
    html.Hr(),
    dcc.Markdown('### Core Competencies', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            dcc.Markdown('''
        * Python Programming
        * Machine Learning
        * Data Exploration & Analysis
        ''')
        ], width={"size": 3, "offset": 1},
            style={'textAlign': 'left'}),
        dbc.Col([
            dcc.Markdown('''
        * Microsoft PowerBI & Excel
        * [Tableau](https://public.tableau.com/app/profile/raimi.azeez.babatunde)
        * SQL & DBMS
        ''')
        ], width=3, style={'textAlign': 'left'}),
        dbc.Col([
            dcc.Markdown('''
        * AWS & Azure Data Studio
        * Leadership
        * Business Strategy
        
        ''')
        ], width=3, style={'textAlign': 'left'})
    ], justify='center'),


    # #Work History
    html.Hr(),
    dcc.Markdown('### Professional Experience', style={'textAlign': 'center'}),
    html.Hr(),
    #Experience 1
    dbc.Row([
        #company, location
        dbc.Row([
            dbc.Col([
                dcc.Markdown('#### Xavier Mcallister Holdings',
                             style={'textAlign': 'left'}),
            ],width = '4'),

            dbc.Col([
                dcc.Markdown('###### Lagos, Nigeria',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify = 'center'),

        # Job Title, Date
        dbc.Row([
            dbc.Col([
                dcc.Markdown('##### Data Scientist',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Dec. 2021 - Present',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),


        # Responsibilities
        dbc.Row([
            dbc.Col([
                html.Ul([
                    html.Li(
                        'I lead the data analytics team in identifying business needs & planning project execution'
                        'to ensure informed and data-driven decision making'),
                    html.Li('I design and develop data management processes and products/apps.'),
                    html.Li('I convert company strategies into automated scripts using historical & technical indicator'
                            ' data with python programming.'),
                ], style={'textAlign': 'left'})
            ], width='8')
        ], justify='center'),
    ]),
    html.Br(),

    # Experience 2
    dbc.Row([
        # company, location
        dbc.Row([
            dbc.Col([
                dcc.Markdown('#### Xavier Mcallister Holdings',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Lagos, Nigeria',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),

        # Job Title, Date
        dbc.Row([
            dbc.Col([
                dcc.Markdown('##### Financial & Investment Data Analyst',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Sept. 2021 - Dec. 2021',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),

        # Responsibilities
        dbc.Row([
            dbc.Col([
                html.Ul([
                    html.Li(
                        'Perform daily trades on provided accounts to build a profitable trading portfolio.'),
                    html.Li('I performed technical & analysis of the financial market.'),
                    html.Li('I analyzed and presently monthly report of trade activities.'),
                ], style={'textAlign': 'left'})
            ], width='8'),
        ], justify='center'),

    ]),
    html.Br(),

    #Experience 3
    dbc.Row([
        #company, location
        dbc.Row([
            dbc.Col([
                dcc.Markdown('#### Hamoye',
                             style={'textAlign': 'left'}),
            ], width = '4'),

            dbc.Col([
                dcc.Markdown('###### Remote',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify = 'center'),

        # Job Title, Date
        dbc.Row([
            dbc.Col([
                dcc.Markdown('##### Data Science Intern',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Sept. 2021 - Nov. 2021',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),


        # Responsibilities
        dbc.Row([
            dbc.Col([
                html.Ul([
                    html.Li(
                        'I Performed exploratory data analysis and visualization to prepare data for modelling.'),
                    html.Li('I Successfully developed machine learning models such as image recognition & time series '
                            'prediction models'),
                    html.Li('I worked with different teams on different case studies, identify machine learning '
                            'solutions to real world problems.'),
                ], style={'textAlign': 'left'})
            ], width='8')

            ], justify='center'),

    ]),
    html.Br(),

    #Experience 4
    dbc.Row([
            #company, location
            dbc.Row([
                dbc.Col([
                    dcc.Markdown('#### Daydream Pictures',
                                 style={'textAlign': 'left'}),
                ], width = '4'),

                dbc.Col([
                    dcc.Markdown('###### Lagos, Nigeria',
                                 style={'textAlign': 'right'})
                ], width='4'),
            ], justify = 'center'),

            # Job Title, Date
            dbc.Row([
                dbc.Col([
                    dcc.Markdown('##### Business Development Executive',
                                 style={'textAlign': 'left'}),
                ], width='4'),

                dbc.Col([
                    dcc.Markdown('###### Sept. 2014 - Sept. 2021',
                                 style={'textAlign': 'right'})
                ], width='4'),
            ], justify='center'),


            # Responsibilities
            dbc.Row([
                dbc.Col([
                    html.Ul([
                        html.Li(
                            'I helped set goals and plans for business revenue and client base growth.'),
                        html.Li('I help maintain client relationship and ensure up to retention up to 10years'),
                        html.Li('I managed its social media from to over 13k+ followers on multiple social media accounts.'),
                    ], style={'textAlign': 'left'})
                ], width='8')

                ], justify='center'),

        ]),
    html.Br(),

    #Education
    html.Hr(),
    dcc.Markdown('### Education', style={'textAlign': 'center'}),
    html.Hr(),

    # Education 1
    dbc.Row([
        # University
        dbc.Row([
            dbc.Col([
                dcc.Markdown('#### WorldQuant University',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Louisiana, USA',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),

        # Course
        dbc.Row([
            dbc.Col([
                dcc.Markdown('###### MSc Financial Engineering',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Jan. 2023 - Present',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),

    ]),
    html.Br(),

    # Education 2
    dbc.Row([
        # University
        dbc.Row([
            dbc.Col([
                dcc.Markdown('#### Ustacky',
                             style={'textAlign': 'left'}),

            ], width='8'),

        ], justify='center'),

        # Course
        dbc.Row([
            dbc.Col([
                dcc.Markdown('###### Data Science MicroDegree',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Mar. 2021 - Jun. 2021',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),

    ]),
    html.Br(),

    # Education 3
    dbc.Row([
        # University
        dbc.Row([
            dbc.Col([
                dcc.Markdown('#### Lagos State University',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Ojo Lagos, Nigeria',
                             style={'textAlign': 'right'})

            ], width='4'),

        ], justify='center'),

        # Course
        dbc.Row([
            dbc.Col([
                dcc.Markdown('###### Fisheries',
                             style={'textAlign': 'left'}),
            ], width='4'),

            dbc.Col([
                dcc.Markdown('###### Apr. 2011 - Jan. 2016',
                             style={'textAlign': 'right'})
            ], width='4'),
        ], justify='center'),

        # Responsibilities
        dbc.Row([
            dbc.Col([
                html.Ul([
                    html.Li(
                        'CGPA 4.37/5.00'),
                ], style={'textAlign': 'left'})
            ], width='8')
        ], justify='center'),

    ]),
    html.Br(),

    # Certifications
    html.Hr(),
    dcc.Markdown('### Certifications', style={'textAlign': 'center'}),
    html.Hr(),
    #Certification 1
    dbc.Row([
        dbc.Col([
            dcc.Markdown('2023',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('###### Business Intelligence & Data Analyst (BIDA)\n',
                         #'San Francisco State University - San Francisco, CA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5),
        dbc.Col([
            dcc.Markdown('Corporate Finance Institute (CFI)',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=3)
    ], justify='center'),

    # Certification 2
    dbc.Row([
        dbc.Col([
            dcc.Markdown('2022',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('###### Financial Modeling & Valuation Analyst (FMVA)\n',
                         # 'San Francisco State University - San Francisco, CA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5),
        dbc.Col([
            dcc.Markdown('Corporate Finance Institute (CFI)',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=3)
    ], justify='center'),

    # Certification 3
    dbc.Row([
        dbc.Col([
            dcc.Markdown('2022',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('###### Machine Learning for Finance (2022)\n',
                         # 'San Francisco State University - San Francisco, CA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5),
        dbc.Col([
            dcc.Markdown('Udemy',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=3)
    ], justify='center'),

    # Certification 4
    dbc.Row([
        dbc.Col([
            dcc.Markdown('2022',
                         style={'textAlign': 'center'})
        ], width=2),
        dbc.Col([
            dcc.Markdown('###### AWS Machine Learning Foundation\n',
                         # 'San Francisco State University - San Francisco, CA',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=5),
        dbc.Col([
            dcc.Markdown('Udacity',
                         style={'white-space': 'pre'},
                         className='ms-3'),
        ], width=3)
    ], justify='center'),

    # Interests
    html.Hr(),
    dcc.Markdown('### Interests', style={'textAlign': 'center'}),
    html.Hr(),
    dbc.Row([
        interests_buttons,
    ], justify='center', className='pt-3'),

])
