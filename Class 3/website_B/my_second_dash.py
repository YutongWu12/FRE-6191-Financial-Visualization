import dash
from dash import dcc, html

# Create an instance of the Dash app, linking the external CSS file
app = dash.Dash(__name__, external_stylesheets=["/assets/my_second_dash.css", "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"])

# Define the layout for the app
app.layout = html.Div([
    # Header with Navigation Bar
    html.Header([
        html.H1("Welcome to My Data Visualization Portfolio"),
        html.Nav([
            html.Ul([
                html.Li(html.A("Home", href="#home")),
                html.Li(html.A("Projects", href="#projects")),
                html.Li(html.A("Contact", href="#contact"))
            ])
        ])
    ], id="header"),
    
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
                    html.Button("View Project")
                ]),
                html.Li([
                    html.H3("Project 2"),
                    html.P("Natural Language Processing for customer feedback."),
                    html.Button("View Project")
                ])
            ])
        ], id="projects"),

        html.Section([
            html.H2("Contact Me"),
            html.Form([
                html.Label("Name:"),
                dcc.Input(type="text", id="name"),
                html.Label("Email:"),
                dcc.Input(type="email", id="email"),
                html.Label("Message:"),
                dcc.Textarea(id="message"),
                html.Button("Submit", type="submit")
            ])
        ], id="contact"),

        # Footer with social media links
        html.Footer([
            html.P("© 2024 Data Visualization Portfolio"),
            html.Div([
                html.A(html.I(className="fab fa-twitter"), href="https://twitter.com", className="icon"),
                html.A(html.I(className="fab fa-linkedin"), href="https://linkedin.com", className="icon"),
                html.A(html.I(className="fab fa-github"), href="https://github.com", className="icon")
            ])
        ], id="footer")
    ])
])

# Run the server with a custom port (e.g., 8051)
app.run_server(debug=True, port=8051)
