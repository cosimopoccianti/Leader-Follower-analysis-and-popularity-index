from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

#The dashboard is also running on https://colab.research.google.com/drive/1BRQDONL646k7R2B5EWH7CinlExgqa281?usp=sharing 

df = pd.read_csv('dataset\quarters.csv', index_col=0)
df['product_id'] = df['product_id'].astype(str)
df['category_1'] = df['category_1'].astype(str)
df['category_2'] = df['category_2'].astype(str)
df['category_3'] = df['category_3'].astype(str)
df['brand'] = df['brand'].astype(str)


app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            "Produtcs popularities"),
        html.P('Deciding on a single criterion to obtain a product ranking seemed reductive for the analysis, as we needed to know the company\'s specific objectives. So we created a dashboard that allows to get the best products depending on the index to apply. \
                This decision was made because it would have been too simple and reductive to sort them into "best-selling" or "highest frequency". We think that an analysis and selection of the best products should be made according to the business objectives. \
                That’s why we have selected different way to rank the products: by profit, quantity, frequency, their mark-up, amount of clicks and stock level. As we know, companies can have different objectives, priorities and needs. One may prefer to focus on \
                the most profitable products because it needs to increase profit; another may concentrate on the best-selling products to increase sales volumes and its network, regardless of how much it earns. The corporate environment is also very dynamic, \
                so depending on the period, the company\'s needs may change. In the first part of the year, the objective may be to increase mark-up, while during November, the focus becomes selling as many products as possible and understanding which products to discount. \
                In this dashboard, there is also the possibility of comparing products with their clicks, allowing understand how effective the bidding strategy is or on which products to apply it. All this depends on the client\'s specific needs, of which we are still unaware, \
                but we think this tool can be very useful to have a better overview.'),
        html.P('The graph provides on the y-axis the products ranked according to the chosen rank, and on the x-axis the values associated with the products (one can for example choose between the quantity sold, the total profit or the number of days the product was sold). \
                The choice of values on the x-axis does not change the products on the y-axis, which depend on the chosen rank. You can then choose to colour the bars according to the categories and brands to which the products belong and the reference quarter (or month of November).'),
        html.Div(
            [
                html.Div(
                    [
                        html.Label("Popularity: here you can choose which way you want to rank the products. The chosen value will rank the products from top to bottom on the y axis. So the highest ranked product will be the first one for the chosen rank."),
                        dcc.Dropdown(
                            id="rank-dropdown",
                            options=['rank_profit','rank_quantity','rank_frequency','rank_regular','rank_bidding','rank_stock','rank_markup'
                            ],
                            value='rank_profit',
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("Values: here you can choose the kind of values for the products ranked as chosen above, which will be displayed in the bars, with the corresponding numbers on the x-axis"),
                        dcc.Dropdown(
                            id="quantity-dropdown",
                            options=['quantity','total_profit','days_sold','total_regular_clicks','total_bidding_clicks','avg_unit_cost','total_stock','avg_%_mark_up'
                            ],
                            value='total_profit',
                            className="dropdown",
                        ),
                    ]
                ),
                html.Div(
                    [
                        html.Label("Category & brand: here you can choose to colour the bars according to category (you can choose first, second or third, depending on the desired granularity) or brand."),
                        dcc.Dropdown(
                            id="category-dropdown",
                            options=['category_1','category_2','category_3','brand'
                            ],
                            value='category_1',
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="row",
        ),
        html.Div(dcc.Graph(id="pop-quarters"), className="chart"),
        html.Label("Quarter: here you can choose for which quarter you want to show the values"),
        dcc.Dropdown(
            id="quarter-dropdown",
            options = ['1st_quarter','2nd_quarter','3rd_quarter','4th_quarter','november'],
        value='1st_quarter',
        ),
    ],
    className="container",
)


@app.callback(
    Output("pop-quarters", "figure"), 
    Input("quarter-dropdown", "value"),
    Input("rank-dropdown", "value"),
    Input("quantity-dropdown","value"),
    Input("category-dropdown","value")
    )

def update_bar_chart(quarter,rank,quantity,category):
    mask = df["quarter"] == quarter
    df1 = df[mask].sort_values(rank).head(20)
    df1.reset_index(inplace=True,drop=True)
    df1.sort_values(rank,inplace=True,ascending=False)
    fig = px.bar(df1, x=quantity, y='product_id', orientation='h',labels={"product_id": "Product ID"}, color=category)
    fig.update_layout(
    barmode='stack', yaxis={'categoryorder':'array', 'categoryarray':df1['product_id']},
    autosize=True,
    height=700,
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
