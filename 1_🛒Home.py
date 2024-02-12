import numpy as np 
import pandas as pd
import plotly.express as px 
import streamlit as st 


st.markdown("<h1 style='text-align: center; color: black;'> E-Commerce  </h1>", unsafe_allow_html=True)
st.image('https://www.redspider.ae/wp-content/uploads/2020/06/ecommerce-seo-tips.jpg')
st.write(''' Data Description:

The dataset contains information related to sales transactions from an e-commerce platform. It includes various attributes that provide insights into the products sold, their prices, quantities, customer locations, and transaction details.

Attributes:

InvoiceNo: A unique identifier for each sales transaction.
UnitPrice: The price per unit of the product in the transaction.
OrderValue: The total value of the order for each transaction, calculated as the unit price multiplied by the quantity.
Quantity: The quantity of products purchased in each transaction.
Country: The country where the transaction occurred.
InvoiceDate: The date when the transaction took place.
InvoiceTime: The time when the transaction occurred.
Year-Month: The year and month of the transaction, formatted for analysis and reporting.
Major Category: The major category of the product sold (e.g., Clothes, Kitchen, Garden).
Minor Category: The minor category of the product sold (e.g., Tops, Shoes, Cutlery).
Description: A brief description of the product included in the transaction.
         
Insights:

The dataset provides a comprehensive overview of sales activities, allowing analysis of sales trends over time and across different product categories.
         
It enables the identification of top-selling products, popular categories, and geographic regions with high sales volumes.
         
Analysis of transaction values and quantities can help identify patterns in customer behavior and preferences.
         
The data can be used to generate insights for inventory management, pricing strategies, and marketing campaigns. 


''')

df = pd.read_csv(r"C:\Users\fg\Downloads\ecommerce.csv")
