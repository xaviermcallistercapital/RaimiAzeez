
import dash
from dash import Dash, html, dcc, ctx, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import dash_loading_spinners as dls

from .side_bar import sidebar
from .kmeans import process_customer, process_credit, build_model, build_credit_model

dash.register_page(__name__, name='K-Means Clustering')

df = process_customer()
df_cc = process_credit()

data_options = [{'label': 'Customer Clustering', 'value': 'df'},
                {'label': 'Credit Card Segmentation', 'value': 'df_cc'}]

tabs = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Clusters", tab_id="cluster"),
                dbc.Tab(label="Optimal K", tab_id="optimal-k"),
                dbc.Tab(label="Custer Distribution", tab_id="cluster-dist"),
                # dbc.Tab(label="Model Diagnostics", tab_id="model-diagnostics"), #model-diagnostics
                # dbc.Tab(label="Model Forecast", tab_id="model-forecast"),
            ],
            id="tabs_classifier",
            # active_tab="chart",
        ),

        html.Br(),

        dls.Hash(html.Div(id="chart-content-div"),
                 color="#435278",
                 speed_multiplier=2,
                 size=50, ),
    ]
)

def layout():
    return dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar()
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    html.H1("K-Means Clustering"),
                    html.P('ARIMA is a Time series forecasting model which......'
                           'Time series forecasting model which......'
                           'Time series forecasting model which......'
                           , style={'textAlign': 'left'}),

                    dcc.Markdown('''
                                   What happened in Africa? Why was the spread so limited compared to other parts of the world?
                                   * Inaccurate/inconsistent data reporting?'
                                   * Early herd Immunity?'
                                   * Natural resistance to the virus?
                                   ''', style={'textAlign': 'left'}),

                    html.Hr(),
                    # dcc.Interval(
                    # id="interval", interval=1000, n_intervals=0),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.Label("Select Dataset:"),
                                    dcc.Dropdown(
                                        id="dataset",
                                        options=data_options,
                                        value='df',
                                    ),
                                ],
                                md=3,
                            ),
                            dbc.Col(
                                [
                                    html.Label("Feature Selection:"),
                                    dcc.Dropdown(
                                        id="feature-selection",
                                        options=[{'label': 'PCA', 'value': True}, {'label': 'No PCA', 'value': False}],
                                        value=False,
                                    ),
                                ],
                                md=2,
                            ),

                            dbc.Col(
                                [
                                    html.Label("K-value: "),
                                    dbc.Input(id='k-value', type='number',
                                              min=1, max=100,
                                              value=4,
                                              ),
                                ],
                                md=2,
                            ),
                            html.Hr(),
                            html.Br(),
                            dbc.Row(
                                [tabs]
                                )],
                        className='align-items-end', justify='center',
                    )
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
    ], fluid=True, class_name='g-0') # p-4


@callback(
    Output("chart-content-div", "children"),
    # Output('price-plot-div', 'src'),
    # Input("interval", "n_intervals"),
    Input("tabs_classifier", "active_tab"),
    Input('dataset', 'value'),
    Input('feature-selection', 'value'),
    Input('k-value', 'value'),

)
def classifier(tab, dataset, pca, k):
    if dataset == 'df':
        if pca:

            elbow_fig_pca, sil_pca, fig_pca, clust_fig_pca = build_model(df, optimal_k=k, pca=True)

            if tab == "cluster":
                graph = dcc.Graph(figure=fig_pca)

                return graph

            elif tab == "optimal-k":

                graph = dcc.Graph(figure=elbow_fig_pca)

                return graph


            elif tab == "cluster-dist":

                graph = dcc.Graph(figure=clust_fig_pca)

                return graph

        else:

            elbow_fig, sil, fig, clust_fig = build_model(df, optimal_k=k, pca=False)

            if tab == "cluster":
                graph = dcc.Graph(figure=fig)

                return graph

            elif tab == "optimal-k":

                graph = dcc.Graph(figure=elbow_fig)

                return graph


            elif tab == "cluster-dist":

                graph = dcc.Graph(figure=clust_fig)

                return graph


    elif dataset == 'df_cc':

        if pca:

            elbow_fig_pca, sil_pca, fig_pca, clust_fig_pca = build_credit_model(df_cc, optimal_k=k, pca=True)

            if tab == "cluster":
                graph = dcc.Graph(figure=fig_pca)

                return graph

            elif tab == "optimal-k":

                graph = dcc.Graph(figure=elbow_fig_pca)

                return graph


            elif tab == "cluster-dist":

                graph = dcc.Graph(figure=clust_fig_pca)

                return graph

        else:

            elbow_fig, sil, fig, clust_fig = build_credit_model(df_cc, optimal_k=k, pca=False)

            if tab == "cluster":
                graph = dcc.Graph(figure=fig)

                return graph

            elif tab == "optimal-k":

                graph = dcc.Graph(figure=elbow_fig)

                return graph


            elif tab == "cluster-dist":

                graph = dcc.Graph(figure=clust_fig)

                return graph
