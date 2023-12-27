import plotly.graph_objs as go
import numpy as np
from plotly.subplots import make_subplots

# Generate data for animation
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
time = np.linspace(0, 10, 100)

# Create figure with subplots
fig = make_subplots(rows=2, cols=1)

# Add trace for x vs y animation
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(width=2, color='blue')), row=1, col=1)

# Add trace for time vs x
fig.add_trace(go.Scatter(x=time, y=x, mode='lines', line=dict(width=2, color='red')), row=2, col=1)



# Add animation
fig.update_layout(
    updatemenus=[
        dict(
            type='buttons',
            showactive=False,
            buttons=[dict(
                label='Play',
                method='animate',
                args=[None, dict(frame=dict(duration=50, redraw=True), fromcurrent=True, mode='immediate', transition=dict(duration=0))]
            ),
                    dict(
                label='Pause',
                method='animate',
                args=[[None],dict(frame=dict(duration=0, redraw=True),mode='immediate',transition=dict(duration=0))]
            )]
        )
    ]
)

# Create frames for animation
frames=[go.Frame(data=[go.Scatter(x=x[:i], y=y[:i],mode='lines')]) for i in range(1,100)]

fig.frames=frames

# Show figure
# fig.show()
fig.to_html('test3_plotly.html')
