import numpy as np 
import pandas as pd
import plotly.express as px 
import streamlit as st
df = pd.read_csv(r"C:\Users\fg\Downloads\ecommerce.csv")
categorical_cols = df.select_dtypes(include='O').columns
numeric_cols = df.select_dtypes(include='number').columns
df['Month'] =pd.to_datetime(df['Year-Month']).dt.month
Months_high_demand = df.groupby('Month')['OrderValue'].count().reset_index()
Months_high_demand.columns = ['Month','Count Of Orders']
fig = px.line(Months_high_demand,x='Month',y='Count Of Orders')
st.write('Here is an overview on our orders during months')
st.plotly_chart(fig)
select_country = st.selectbox("select country to filter by ",df['Country'].unique())
df_filtered = df[df['Country']==select_country]
Months_high_demand = df_filtered.groupby('Month')['OrderValue'].count().reset_index()
Months_high_demand.columns = ['Month','Count Of Orders']
fig = px.line(Months_high_demand,x='Month',y='Count Of Orders')
st.write(f'Here is an overview on our orders in {select_country} during months')
st.plotly_chart(fig)