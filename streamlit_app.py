import streamlit as st
import pandas as pd
import plotly.express as px



DATE_COLUMN = 'date'
DATA_URL = 'data.csv'

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data


data = load_data(1000)
ycols = data.columns.values.tolist()

fig = px.box(data,x='date',y=ycols[1:])


st.title('Ranking Fluctuations for All Sites')
st.plotly_chart(fig, theme='streamlit', use_container_width=True)
