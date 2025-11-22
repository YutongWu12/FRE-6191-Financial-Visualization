import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Population': [8.4, 4.0, 2.7, 2.3, 1.7],
    'Area': [783.8, 1214.9, 589.6, 1651.1, 1340.6]
})

# Create a scatter plot
fig = px.scatter(df, x='Area', y='Population', size='Population', color='City',
                 title='City Population vs Area')

# Customize the hover tooltip
fig.update_traces(
    hovertemplate='<b>%{text}</b><br>Population: %{y}M<br>Area: %{x} km²',
    text=df['City']
)

fig.show()
