# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
#df = pd.DataFrame({
 #   "Product": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
 #   "Date": [4, 1, 2, 2, 4, 5],
#  "Region": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
#})
df1 = pd.read_csv('combined_file.csv')
df1 = df1.sort_values(by='date', ascending=True)

#fig1 = px.scatter(df1, x="Sales", y="date",
                 #size="Sales", color="region", hover_name="region",
                 #log_x=True, size_max=60)
fig1 = px.line(df1, x="date", y="Sales",color="region", hover_name="region")
#fig1 = px.bar(df, x="Product", y="date", color="region", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Soul Foods’s Data Visualization', style={'color': 'white',
    'text-align':'center',
    'background-color':'grey'}),

    html.Div(children='''
        Product : Visualization of Pink Morsel sales by region within the defferents periods
    ''', style={'text-align': 'center',
    'text-decoration':'underline'}),

    dcc.Graph(
        id='example-graph',
        figure=fig1,
        #id1='example-graph1',
        #figure1=fig1
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)
