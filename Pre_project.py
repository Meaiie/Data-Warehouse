import streamlit as st
import pandas as pd
import plotly.express as px

# Sample sales data with two measures (sales and quantity)
data = pd.DataFrame({
'region': ['North America', 'North America', 'North America', 'South America', 'South America', 'Europe', 'Europe', 'Asia', 'Asia'],
'country': ['USA', 'Canada', 'Mexico', 'Brazil', 'Argentina', 'Germany', 'France', 'China', 'India'],
'product': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E'],
'sales': [100, 150, 200, 250, 300, 350, 400, 450, 500],
'quantity': [10, 15, 20, 25, 30, 35, 40, 45, 50]
})

# Title of the dashboard
st.title('Sales Data Cube Viewer Dashboard')

st.sidebar.header('Filter Options')
region_filter = st.sidebar.multiselect('Select Region(s):', options=data['region'].unique(), default=data['region'].unique())
country_filter = st.sidebar.multiselect('Select Country(s):', options=data['country'].unique(), default=data['country'].unique())
product_filter = st.sidebar.multiselect('Select Product(s):', options=data['product'].unique(), default=data['product'].unique())

# Applying filters to the data
filtered_data = data[
(data['region'].isin(region_filter)) &
(data['country'].isin(country_filter)) &
(data['product'].isin(product_filter))
]

st.header('Sales Data Visualization')

# Aggregation
agg_data = filtered_data.groupby(['region', 'country', 'product']).sum().reset_index()

# Sunburst Chart for Sales
st.subheader('Sales by Region, Country, and Product (Sunburst Chart)')
sunburst_sales = px.sunburst(
agg_data,
path=['region', 'country', 'product'],
values='sales',
title='Sales by Region, Country, and Product'
)
st.plotly_chart(sunburst_sales)

# Treemap Chart for Quantity
st.subheader('Quantity by Region, Country, and Product (Treemap Chart)')
treemap_quantity = px.treemap(
agg_data,
path=['region', 'country', 'product'],
values='quantity',
title='Quantity by Region, Country, and Product'
)
st.plotly_chart(treemap_quantity)

# Bar Chart for both Sales and Quantity
st.subheader('Sales and Quantity by Country and Product')
bar_sales_quantity = px.bar(
agg_data,
x='country',
y=['sales', 'quantity'],
color='product',
title='Sales and Quantity by Country and Product',
barmode='group'
)
st.plotly_chart(bar_sales_quantity)

# Display filtered aggregated data table
st.header('Aggregated Filtered Data')
st.write(agg_data)

if st.sidebar.button('Show Info'):
   st.sidebar.write('This is a demo of a hierarchical data visualization using Streamlit and Plotly, showing Sales and Quantity by Region and Product.')