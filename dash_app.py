from dash import Dash, Input, html, dcc, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/pink_morsel_sales_data.csv')

app.layout = html.Div(
    className='background',
    children=[
        html.H1(children='Pink Morsel Sales Dashboard', id='header', className='text'),

        dcc.Graph(
            id='pink-morsel-sales-graph'
        ),

        dcc.RadioItems(
            id='region-selector',
            options=[
                {'label': 'All Regions', 'value': 'all'},
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'}
            ],
            value='all'
        )
    ]
)

@app.callback(
    Output('pink-morsel-sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]

    filtered_df = filtered_df.groupby('date')['sales'].sum().reset_index()

    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title='Pink Morsel Sales Over Time'
    )
    
    fig.update_traces(
        line=dict(color='#ff69b4', width=2)
    )
    
    fig.update_layout(
        plot_bgcolor='#1f1f1f',   
        paper_bgcolor='#1f1f1f',
        font_color='#bebdbd',    
        margin=dict(t=50, b=40, l=50, r=20), 
        xaxis=dict(
            showgrid=True, 
            gridcolor='#2d2d2d'  
        ),
        yaxis=dict(
            showgrid=True, 
            gridcolor='#2d2d2d'   
        )
    )
    
    return fig

if __name__ == '__main__':
    app.run(debug=True)
