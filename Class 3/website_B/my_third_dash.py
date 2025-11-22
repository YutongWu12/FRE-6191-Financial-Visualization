import dash
import os
from dash import html

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=["/assets/my_third_dash.css", "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"])

# Serve the static HTML file (index.html) via Dash
app.layout = html.Div([
    # Load the index.html page
    html.Iframe(srcDoc=open(os.path.join(os.getcwd(), "my_third_dash.html")).read(), style={'width': '100%', 'height': '100vh', 'border': 'none'})
])

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
