import numpy as np 
import pandas as pd
import plotly.express as px 
import streamlit as st
df = pd.read_csv("ecommerce.csv")
categorical_cols = df.select_dtypes(include='O').columns
numeric_cols = df.select_dtypes(include='number').columns
user_feature = st.selectbox("Select a feature you want to see it's graph with the major categories ",['UnitPrice', 'OrderValue', 'Quantit'])
df_2 = df.groupby('Major Category')[user_feature].mean().reset_index()
fig = px.bar(df_2,x='Major Category', y= user_feature,color='Major Category',color_discrete_sequence=px.colors.sequential.Electric_r)
st.plotly_chart(fig)
select_country = st.selectbox("select country to filter by ",df['Country'].unique())
df_filtered = df[df['Country']==select_country]
user_feature = st.selectbox(f"Select a feature you want to see it's graph in {select_country} with the major categories ",['UnitPrice', 'OrderValue', 'Quantit'])
df_2 = df_filtered.groupby('Major Category')[user_feature].mean().reset_index()
fig = px.pie(df_2,names='Major Category', values= user_feature,color='Major Category',color_discrete_sequence=px.colors.sequential.Electric_r,hole=0.5)
st.plotly_chart(fig)
df_2 = df.groupby('Major Category')[user_feature].mean().reset_index()
fig = px.bar(df,x='Major Category', y= user_feature,color='Minor Category',barmode='group',color_discrete_sequence=px.colors.sequential.Electric_r)
st.plotly_chart(fig)
