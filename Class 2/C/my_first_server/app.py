import dash
from dash import html
import os

# Initialize the Dash app
app = dash.Dash(__name__, suppress_callback_exceptions=True)

# Path to the HTML file (relative to the project folder)
html_file_path = os.path.join(os.path.dirname(__file__), 'index.html')

# Read the HTML content
with open(html_file_path, 'r') as file:
    html_content = file.read()

# Define the layout of the Dash app
app.layout = html.Div([
    html.Iframe(srcDoc=html_content, width="100%", height="1000px")
])

# Run the server
if __name__ == '__main__':
    app.run_server(debug=True)
