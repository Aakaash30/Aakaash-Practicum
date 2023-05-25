import streamlit as st
import pandas as pd
import plotly.express as px

vehicles_df = pd.read_csv('c:/Users/aakaa/OneDrive/Documents/Aakaash-Practicum/vehicles_us.csv')

st.header('Vehicle Market')

#Fills missing values in 'is_4wd' column with '2wd' and converts entire column to string type
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].fillna('2wd').astype('str')

#Replaces values of 1 (assuming 1 = vehicle is 4wd) with '4wd'
vehicles_df['is_4wd'] = vehicles_df['is_4wd'].replace(['1.0'], '4wd')

#Scatterplot of model year vs price for each vehicle type
fig = px.scatter(vehicles_df, x="price", y="model_year", color="is_4wd")
fig.update_layout(xaxis_title="Price", yaxis_title="Model Year")
st.plotly_chart(fig, use_container_width=True)

check_box_4wd = st.checkbox('Display of 4wd vehicles', value=True)

if check_box_4wd:
    pc_df = vehicles_df.loc[vehicles_df['is_4wd'] == '4wd']  
elif not check_box_4wd:
    pc_df = vehicles_df

#histogram settings    
fig = px.histogram(pc_df, title='Number of vehicles with specific drivetrain vs. Price', x='price', color='is_4wd', nbins=50, barmode='overlay')
fig.update_layout(xaxis_title="Price", yaxis_title="Number of Vehicles", yaxis_range=[0,5000], xaxis_range=[0,100000])
# showing the histogram of drivetrain vs price
st.plotly_chart(fig, use_container_width=True)

st.write("Average price against each vehicle condition.")

#Plot of the average price against the vehicle's condition
price_condition_df = vehicles_df.groupby('condition')['price'].mean().round(0).astype('int')

fig = px.bar(price_condition_df, y="price",
title="Vehicle's average price against vs vehicle's condition", color="price",
labels={"price": "Average price (USD)", "condition": "Vehicle's condition"})
fig.update_xaxes(categoryorder='array', categoryarray= ['new', 'like new', 'excellent', 'good', 'fair', 'salvage'])
fig.update(layout_coloraxis_showscale=False)
st.plotly_chart(fig, use_container_width=True)

#Plot of the vehicle's average price against the car model
price_model_df = vehicles_df.groupby('model')['price'].mean().round(0).astype('int')

fig = px.bar(price_model_df, y="price",
title="Vehicle's average price against vs vehicle's model", color="price",
labels={"price": "Average price (USD)", "condition": "Vehicle's model"})
fig.update(layout_coloraxis_showscale=False)
st.plotly_chart(fig, use_container_width=True)