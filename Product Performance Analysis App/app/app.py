import base64
from io import BytesIO

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
from wordcloud import WordCloud


final_ads_to_model = pd.read_csv('final_data_till_Aug_Flag_with_adj_1.csv', encoding='latin')
predict_file =pd.read_csv('final_output_Oct_final.csv', encoding='latin')
final_ads_df = pd.read_csv('final_ads_till_Aug.csv', encoding='latin')
total_sales = final_ads_to_model['invoice_price'].sum()
total_customers = len(final_ads_to_model['cust_sku'].unique())
total_products = len(final_ads_to_model['ITEMID'].unique())


def Header(name, app):
    title = html.H2(name, style={'margin-top': 5})
    encoded_image = base64.b64encode(open('assets/logo.png', 'rb').read())
    logo = html.Img(
        src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'float': 'right', 'height': 50}
    )

    return dbc.Row([dbc.Col(title, md=9), dbc.Col(logo, md=3)])


def plot_wordcloud(data,colname):
    d = data[colname].value_counts().to_dict()
    wc = WordCloud(background_color='black', width=400, height=400)
    wc.fit_words(d)
    return wc.to_image()


cards = [
    dbc.Card(
        [
            html.H2(f'{total_sales:.2f}', className='card-title'),
            html.P('Total Sales', className='card-text'),
        ],
        body=True,
        color='light',
    ),
    dbc.Card(
        [
            html.H2(f'{total_customers}', className='card-title'),
            html.P('Total Customers', className='card-text'),
        ],
        body=True,
        color='dark',
        inverse=True,
    ),
    dbc.Card(
        [
            html.H2(f'{total_products}', className='card-title'),
            html.P('Total Products', className='card-text'),
        ],
        body=True,
        color='primary',
        inverse=True,
    ),
]


graphs=[[html.Label('Select a Region:'),
          dcc.Dropdown(
              id='w_countries',
              multi=False,
              clearable=True,
              value=final_ads_to_model['REGION'].min(),
              placeholder='Select region',
              options=[{'label': c, 'value': c} for c in (final_ads_to_model['REGION'].unique())]
        ),   
        html.Br(),
        dcc.Graph(id='bar_line_1')],
        [
            html.Label('Select a year:'),
            dcc.Dropdown(
                id='years',
                multi=False,
                clearable=True,
                value=final_ads_to_model['year'].min(),
                placeholder='Select year',
                options=[{'label': c, 'value': c} for c in (final_ads_to_model['year'].unique())], 
            ),
        html.Br(),
        dcc.Graph(id='bar_line_2')],
]

graphs1 = [[dcc.Graph(id='line-chart-1')],
    [dcc.Graph(id='line-chart-2')]]


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server
app.title = 'Product Performance Analysis App'
app.css.config.serve_locally = False
app.config.suppress_callback_exceptions = True

summary = '''
This App is a Analytic Dashboard presents yearly product performance, product category, 
Top Customers and product performance by the regions to help businesses 
identifying the product segments and categories that have met or exceeded their expectations.
'''

app.layout =dbc.Container(
    [
        html.Br(),
        Header('Product Performance Analysis', app),
        html.Hr(),
        html.H4(summary),
        html.Br(),
        dbc.Row([dbc.Col(card) for card in cards]),
        html.Br(),
        dbc.Row([dbc.Col(graph) for graph in graphs]),
        html.Br(),
        dcc.RadioItems(
            id='checklist',
            options=[{'label': c, 'value': c} for c in (final_ads_df['REGION'].unique())],
            value=final_ads_df['REGION'].unique()[0],
            labelStyle={
                'display': 'inline-block',
                'margin-right': '7px',
                'font-weight': 300
            },
            style={
                'display': 'inline-block',
                'margin-left': '7px'
            }
        ),
        html.Br(),
        dbc.Row([dbc.Col(graph) for graph in graphs1]),
        html.Br(),
        dbc.Row([dbc.Col(
        html.Div(
            [
                html.H2('Top Products:'),
                html.Img(id='image_wc')
            ]
        )),
        dbc.Col(
        html.Div([
            html.H2('Top Customers:'),
            html.Img(id='image_wc_1')
        ]))]),    
        html.Br(),                
        html.Div([
            html.H1('Prediction for Next 5 Months'),
            html.Label('Select Product:'),
            dcc.Dropdown(
                id='product',
                multi=False, 
                clearable=True,
                value=predict_file['cust_sku'].unique()[0], 
                placeholder='Select region',
                options=[{'label': c, 'value': c} for c in (predict_file['cust_sku'].unique())]
            ),
            dcc.Graph(
                id='line_line_5', 
                config={'displayModeBar': False}
            ),
        ])                   
    ],
    fluid=False,
)


@app.callback([Output('bar_line_1', 'figure'),Output('bar_line_2', 'figure')],
              [Input('w_countries', 'value'),Input('years', 'value')])
def update_graph(w_countries,years):
# Data for bar
    if w_countries or years:
        print(w_countries)
        print(years)
        product_sales1 = final_ads_to_model.groupby(['REGION', 'ITEMID'])['order_qty'].sum().reset_index()
        product_sales = final_ads_to_model.groupby(['year', 'REGION'])['invoice_price'].sum().reset_index()
        product_sales1 = product_sales1[product_sales1['REGION'] == w_countries]
        product_sales =product_sales[product_sales['year'] == years]
        print(product_sales.columns)
        print(product_sales1.columns)
        fig1 = px.bar(product_sales1, x='ITEMID', y='order_qty')
        fig2 = px.bar(product_sales, x='REGION', y='invoice_price')
        fig1.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        fig2.update_layout(margin=dict(t=0, b=0, l=0, r=0))
        fig1.update_xaxes(tickangle=-90)
        return fig1, fig2
        

@app.callback(
    [Output('line-chart-1', 'figure'), Output('line-chart-2', 'figure')],
    [Input('checklist', 'value')])
def update_line_chart(w_countries):
    product_sales = final_ads_df.groupby(['REGION', 'ORDERDATE'])['Order QTY in Base Unit'].sum().reset_index()
    product_sales1 = final_ads_df.groupby(['REGION', 'ORDERDATE'])['Net Value In Local'].sum().reset_index()
    product_sales = product_sales[product_sales['REGION']==w_countries]
    product_sales1 = product_sales1[product_sales1['REGION']==w_countries]
    fig1 = px.line(product_sales, 
        x='ORDERDATE', y='Order QTY in Base Unit', color='REGION')
    fig1.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    fig2 = px.line(product_sales1, 
        x='ORDERDATE', y='Net Value In Local', color='REGION') 
    fig2.update_layout(margin=dict(t=0, b=0, l=0, r=0))
    return fig1, fig2


@app.callback(Output('image_wc', 'src'), [Input('image_wc', 'id')])
def make_image(b):
    img = BytesIO()
    plot_wordcloud(data=final_ads_df, colname='ItemName').save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())    


@app.callback(Output('image_wc_1', 'src'), [Input('image_wc_1', 'id')])
def make_image(b):
    img = BytesIO()
    plot_wordcloud(data=final_ads_df, colname='CUSTNAME').save(img, format='PNG')
    return 'data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())


@app.callback(
    Output('line_line_5', 'figure'), 
    [Input('product', 'value')])
def update_line_chart(ticker):
    predict_file1 = predict_file[predict_file['cust_sku']==ticker]
    
    # fig
    return px.line(predict_file1, x='month', y='predicted')

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=False) 
