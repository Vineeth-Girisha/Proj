import pandas as pd
# import sqlalchemy as sa
import plotly.express as px
import plotly.graph_objects as go
# import gif
import io
import PIL



with pd.ExcelFile(r"C:\Users\600305138\Desktop\VS code\required rows1.xlsx") as data:
    date= pd.read_excel(data,"Sheet2",header=[1], usecols=[8,9])
    month= pd.read_excel(data,"Sheet2", header=[1], usecols=[15,16,17])
    Request_reason= pd.read_excel(data, "Sheet2", header=[1], usecols=[11,12])




fig = go.Figure(data=px.choropleth(
    locations=month['state'], 
    color = month['hikes'].astype(float),
    locationmode = 'USA-states',
    animation_frame=month['month'],
    color_continuous_scale=px.colors.cyclical.IceFire
))

fig.update_layout(
    title_text = 'Hiking heatmap',
    geo_scope='usa', 
)
fig.show()
frames = []
# for s, fr in enumerate(fig.frames):
#     # set main traces to appropriate traces within plotly frame
#     fig.update(data=fr.data)
#     # move slider to correct place
#     fig.layout.sliders[0].update(active=s)
#     # generate image of current state
#     frames.append(PIL.Image.open(io.BytesIO(fig.to_image(format="png"))))
    
# # create animated GIF
# frames[0].save(
#         "test.gif",
#         save_all=True,
#         append_images=frames[1:],
#         optimize=True,
#         duration=500,
#         loop=0,
#     )

chart= px.line(date, x='MONTH', y='Count of HIKE_REQUEST_ID.2')


Req_res= px.bar(Request_reason, x='Request Reason', y='Count of HIKE_REQUEST_ID.3')


# from plotly._subplots import make_subplots

# dash= make_subplots(rows=1, cols=2)
# dash = tools.make_subplots(rows=1,cols=1, vertical_spacing=0.5)
# dash.add_trace(px.scatter(month, x='MONTH', y='Count of HIKE_REQUEST_ID.2'), row=1, col=1)
# dash.add_trace(px.bar(Request_reason, x='Request Reason', y='Count of HIKE_REQUEST_ID.3'), row=1, col=2)
# dash.show()

# from plotly.subplots import make_subplots
# finfig = make_subplots(
#     rows=2, cols=2,
#     specs=[[{'type': 'choropleth'},   None  ],
#             [          {'type': 'xy'}       , {'type': 'xy'}]])
 


# finfig.add_trace(fig['data'][0], row=1, col=1)
# finfig.add_trace(chart['data'][0], row=2, col=1)
# finfig.add_trace(Req_res['data'][0], row=2, col=2)


# finfig.update_layout(
#     title="HIKING DATA",
# showlegend=True,
# height=800
# )
# finfig.update_layout(
#     title_text = 'Hiking heatmap',
#     geo_scope='usa', 
# )
# finfig.show()



# from dash import Dash, dcc, html

# app= Dash()
# app.layout= [html.Div([
#     html.Div([
#         dcc.Graph(figure=fig)
#     ]),

#     html.Div([
#         dcc.Graph(figure=Req_res),
#         dcc.Graph(figure=chart)
#     ], style={'width':'49%'}),
    
#     ]
#     )

# ]


# app.run_server(debug=True, use_reloader=False)