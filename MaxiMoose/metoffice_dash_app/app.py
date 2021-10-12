from os import path
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

import weather_data as wd
import data_processor as dp

app = dash.Dash(__name__)


app.layout = html.Div(children=[
    html.H1(children='Dash: A web application framework for data'),

    html.Div(children='''
        
    '''),
    dcc.Dropdown(id='dropdown_station', options=[
            {'label': 'Cardiff', 'value': 'cardiffdata.txt'},
            {'label': 'Eastbourne', 'value': 'eastbournedata.txt'},
            {'label': 'Lerwick', 'value': 'lerwickdata.txt'}],
            value = 'Cardiff'),

    dcc.Graph(
        id='graph1'
    ),
        html.Div(children='''
        
    '''),

    dcc.Graph(
        id='graph2'
    )
])

@app.callback(
    dash.dependencies.Output('graph1', 'figure'),
    dash.dependencies.Output('graph2', 'figure'),
    dash.dependencies.Input('dropdown_station', 'value'))
def update_figure(selected_station):

    data_caller = wd.weatherData()
    #Metoffice page here - https://www.metoffice.gov.uk/research/climate/maps-and-data/historic-station-data

    metoffice_data = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/stationdata/'

    data_caller.build_data(path=metoffice_data+selected_station)

    df_builder = dp.dataProcessor()
    df_averages = df_builder.build_df()

    fig1 = px.line(df_averages, x="Month", y="Rain")
    fig1.update_layout(title='Average Rainfall ',
                   xaxis_title='Month',
                   yaxis_title='Rainfall (mm)')

    fig2= px.line(df_averages, x="Month", y=["T Max","T Min"])
    fig2.update_layout(title='Average Maximum and Minimum Temperatures ',
                   xaxis_title='Month',
                   yaxis_title='Temperature (degrees C)')

    return fig1, fig2


if __name__ == '__main__':
    app.run_server(debug=True)