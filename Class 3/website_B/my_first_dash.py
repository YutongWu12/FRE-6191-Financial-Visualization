import dash
from dash import dcc, html

# Create an instance of the Dash app
app = dash.Dash(__name__, external_stylesheets=["https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"])

# Define the layout for the app
app.layout = html.Div([
    # Header with Navigation Bar
    html.Header([
        html.H1("Welcome to My Data Visualization Portfolio"),
        html.Nav([
            html.Ul([
                html.Li(html.A("Home", href="#home", style={'color': '#ADD8E6', 'text-decoration': 'none'})),  # Light Blue color for Home
                html.Li(html.A("Projects", href="#projects", style={'color': '#ADD8E6', 'text-decoration': 'none'})),  # Light Blue color for Projects
                html.Li(html.A("Contact", href="#contact", style={'color': '#ADD8E6', 'text-decoration': 'none'}))  # Light Blue color for Contact
            ], style={'display': 'flex', 'list-style-type': 'none', 'justify-content': 'center', 'gap': '20px'})  # Flexbox for horizontal layout
        ])
    ], style={'background-color': '#2c3e50', 'color': 'white', 'padding': '20px', 'text-align': 'center'}),  # Header styles
    
    # Main content with sections
    html.Main([
        html.Section([
            html.H2("Introduction"),
            html.P("I was first introduced to Data Visualization by Prof. Yarmish...")
        ], id="intro"),

        html.Section([
            html.H2("My Data Visualization Projects"),
            html.Ul([
                html.Li([
                    html.H3("Project 1"),
                    html.P("Predictive analytics for sales data."),
                    html.Button("View Project", style={'background-color': '#3498db', 'color': 'white', 'padding': '10px 20px', 'border': 'none', 'cursor': 'pointer', 'font-size': '1rem', 'transition': 'background-color 0.3s ease'})
                ]),
                html.Li([
                    html.H3("Project 2"),
                    html.P("Natural Language Processing for customer feedback."),
                    html.Button("View Project", style={'background-color': '#3498db', 'color': 'white', 'padding': '10px 20px', 'border': 'none', 'cursor': 'pointer', 'font-size': '1rem', 'transition': 'background-color 0.3s ease'})
                ])
            ], style={'display': 'flex', 'justify-content': 'space-between', 'gap': '20px', 'list-style-type': 'none'})  # Flexbox for horizontal layout of projects
        ], id="projects"),

        html.Section([
            html.H2("Contact Me"),
            html.Form([
                html.Label("Name:"),
                dcc.Input(type="text", id="name", style={'padding': '10px', 'font-size': '1rem', 'border': '1px solid #ccc', 'border-radius': '4px'}),
                html.Label("Email:"),
                dcc.Input(type="email", id="email", style={'padding': '10px', 'font-size': '1rem', 'border': '1px solid #ccc', 'border-radius': '4px'}),
                html.Label("Message:"),
                dcc.Textarea(id="message", style={'padding': '10px', 'font-size': '1rem', 'border': '1px solid #ccc', 'border-radius': '4px', 'resize': 'vertical', 'min-height': '100px'}),
                html.Button("Submit", type="submit", style={'background-color': '#3498db', 'color': 'white', 'padding': '10px', 'border-radius': '4px', 'cursor': 'pointer'})
            ], style={'display': 'flex', 'flexDirection': 'column', 'gap': '15px', 'maxWidth': '400px', 'margin': '0 auto'})  # Flexbox for vertical stack
        ], id="contact"),

        # Footer with social media links
        html.Footer([
            html.P("© 2024 Data Visualization Portfolio"),
            html.Div([
                html.A(html.I(className="fab fa-twitter"), href="https://twitter.com", className="icon", style={'color': 'white', 'margin': '0 10px'}),
                html.A(html.I(className="fab fa-linkedin"), href="https://linkedin.com", className="icon", style={'color': 'white', 'margin': '0 10px'}),
                html.A(html.I(className="fab fa-github"), href="https://github.com", className="icon", style={'color': 'white', 'margin': '0 10px'})
            ], style={'text-align': 'center', 'padding': '20px'})
        ], style={'background-color': '#2c3e50', 'color': 'white', 'text-align': 'center', 'padding': '20px'})
    ])
])

# Run the server with a custom port (e.g., 8051)
app.run_server(debug=True, port=8051)
