import streamlit as st
import pandas as pd
import numpy as np
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title("Flights Analytics")
user_option=st.sidebar.selectbox('menu', ['select one','check flights','analytics'])
if user_option=="check flights":
    st.title("check flights")
    col1,col2 = st.columns(2)
    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source',sorted(city))
    with col2:
        destination = st.selectbox('Destination', sorted(city))
    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        #results['Dep_Time'] = results['Dep_Time'].astype(str)
        #st.dataframe(['Airline','Route,Price','Date_of_Journey'])
        st.dataframe(results)

elif user_option=="analytics":
    st.title("analytics")
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)
else:
    pass