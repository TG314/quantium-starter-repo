from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv('data/pink_morsel_sales_data.csv')

fig = px.line(df, x="date", y="sales", title='Pink Morsel Sales Over Time')

app.layout = html.Div(children=[
    html.H1(children='Pink Moresel Sales Dashboard'),

    html.Div(children='''
        This is a simple dashboard to visualize Pink Morsel sales data over time.
    '''),

    dcc.Graph(
        id='pink-morsel-sales-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)