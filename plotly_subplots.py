import numpy as np
import plotly
import plotly.subplots 
import plotly.graph_objects as go

x    = np.arange(0, 50, 0.01);
sinx = np.sin(x)
cosx = np.cos(x)

np.savetxt('sinx.csv', sinx, delimiter=',')
np.savetxt('cosx.csv', cosx, delimiter=',')

sinx = np.loadtxt('sinx.csv')
cosx = np.loadtxt('cosx.csv')

fig = plotly.subplots.make_subplots(rows=2,cols=1, shared_xaxes=True, vertical_spacing=0.03, x_title='LOG', subplot_titles=['sin'], row_heights=[1,1])
#
fig.add_trace(go.Scatter(x=x,y=sinx,name='sin',mode='lines',line=dict(color='blue')),row=1,col=1)
fig.add_trace(go.Scatter(x=x,y=cosx,name='cos',mode='lines',line=dict(color='red')), row=1,col=1)
#
fig.add_trace(go.Scatter(x=x,y=cosx,name='cos',mode='lines',line=dict(color='blue')),row=2,col=1)
fig.add_trace(go.Scatter(x=x,y=sinx,name='sin',mode='lines',line=dict(color='red')), row=2,col=1)
#
fig.update_layout(hovermode='x unified')
#
fig.write_html('plotly_subplots.html')
