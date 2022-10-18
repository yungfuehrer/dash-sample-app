import dash
from dash import Dash, html, dcc
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px

df = pd.read_csv(r'data/exchange_rates (2).csv',
                 index_col=False)
colors = {
    'background': 'black',
    'text-graphs': '#7FDBFF',
    'line_1': '#DAA520',
    'line_2': '#D84035',
    'text': '#FDFEFE'
}
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])

fig = px.line(df, x='Date', y='EXMP1', markers=True)
fig.update_traces(line_color=colors['line_1'])
fig2 = px.line(df, x='Date', y='EXMP2', markers=True)
fig2.update_traces(line_color=colors['line_2'])
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text-graphs']
)
fig2.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text-graphs']
)
fig.update_xaxes(showgrid=False, zeroline=False, showline=True, linewidth=1, linecolor='white')
fig.update_yaxes(showgrid=False, zeroline=False, showline=True, linewidth=1, linecolor='white')
fig2.update_xaxes(showgrid=False, zeroline=False, showline=True, linewidth=1, linecolor='white')
fig2.update_yaxes(showgrid=False, zeroline=False, showline=True, linewidth=1, linecolor='white')

app.layout = html.Section([
    # THREE ROWS WITH COLUMNS
    html.Div([
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className="card-wrap"
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP2', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP2'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
    ], className='row-wrap'),
    html.Div([
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
    ], className='row-wrap'),
    html.Div([
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
        html.Div([
            html.Div([
                html.H5(children='EXMP1', className='title')
            ], className="title-wrap"),
            html.Div([
                html.H6(children='USD', className='currency'),
                html.P(f"{df['EXMP1'].iloc[-1]:,.0f}",
                       className='current-cost'
                       ),
            ], className="card_container"),
        ], className='card-wrap'
        ),
    ], className='row-wrap'),

    # CROSS LINE
    dbc.Row([
        html.Hr(className='line-scale')
    ]),

    # GRAPHS
    dbc.Row([
        dcc.Graph(
            id='example-graph',
            figure=fig,
            className='graph'
        )
    ]),
    dbc.Row([
        dcc.Graph(
            id='example-graph2',
            figure=fig2,
            className='graph'
        )
    ])
], className='section')

if __name__ == '__main__':
    app.run_server(debug=True)
