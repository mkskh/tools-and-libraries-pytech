import dash
import dash_core_components as dcc
import dash_html_components as html

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Dash App"),
    html.P("Welcome to a basic Dash web application."),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Bar chart'},
            ],
            'layout': {
                'title': 'Bar Chart'
            }
        }
    )
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
