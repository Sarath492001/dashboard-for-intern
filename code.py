import plotly.graph_objects as go
import plotly.io as pio
import pandas as pd

# Sample data
data = [
    {
        'image': 'image1.jpg',
        'title': 'Song 1',
        'unique_plays': 50,
        'total_plays': 100,
        'completion_rate': 75
    },
    {
        'image': 'image2.jpg',
        'title': 'Song 2',
        'unique_plays': 80,
        'total_plays': 120,
        'completion_rate': 60
    },
    {
        'image': 'image3.jpg',
        'title': 'Song 3',
        'unique_plays': 30,
        'total_plays': 50,
        'completion_rate': 90
    }
]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Create graph for unique_plays and total_plays
fig = go.Figure()
fig.add_trace(go.Bar(x=df['title'], y=df['unique_plays'], name='Unique Plays'))
fig.add_trace(go.Bar(x=df['title'], y=df['total_plays'], name='Total Plays'))
fig.update_layout(barmode='group', xaxis_title='Songs', yaxis_title='Plays')

# Create progress bar for completion_rate
progress_bar = go.Figure(go.Indicator(
    mode='gauge+number',
    value=df['completion_rate'][0],
    gauge={'axis': {'range': [None, 100]}, 'bar': {'color': 'purple'}},
    domain={'x': [0, 1], 'y': [0, 1]}
))
progress_bar.update_layout(title='Completion Rate')

# Save the dashboard as an HTML file
pio.write_html(fig, 'dashboard.html')
pio.write_html(progress_bar, 'progress_bar.html')
