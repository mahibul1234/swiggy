import pandas as pd 
import streamlit as st 
import seaborn as sns 
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
st.title("_SWIGGY MARKET SALE DASHBORD_")
st.markdown("---")
df=pd.read_csv('swiggy.csv')
st.table(df.head(3))
st.markdown("----")
avg=round(df['Avg ratings'].mean(),1)
avg_delivery_time = round(df['Delivery time'].mean())
col1,col2=st.columns(2)
with col1:
   st.subheader('AVR_RATING:')
st.subheader(f'{avg}')
with col2:
    st.subheader('avg_delivery_time')
    st.subheader(f' {avg_delivery_time} minutes')
st.markdown('----')

st.sidebar.header('FILTER HERE')
area=st.sidebar.multiselect('selcet Area:',
options=df['Area'].unique(),
default=df['Area'].unique()[:3])


st.sidebar.header('FILTER HERE')
rest=st.sidebar.multiselect('selcet Restaurant:',
options=df['Restaurant'].unique(),
default=df['Restaurant'].unique()[:3])

df_selection = df.query(
    "Area == @area  & Restaurant == @rest"
)


total_sale=pd.pivot_table(df_selection, index='Area', values='Price', aggfunc='sum')
total=pd.pivot_table(df_selection, index='Restaurant', values='Price', aggfunc='sum')
st.markdown("----")
col3,col4=st.columns(2)
with col3:
    st.table(total_sale)

with col4:
    st.table(total)    
st.markdown("-----")
total_sale=pd.pivot_table(df_selection, index='Area', values='Price', aggfunc='sum').sort_values(by='Price')
total=pd.pivot_table(df_selection, index='Area', values='Price', aggfunc='sum').reset_index()

fig = px.bar(total_sale, x='Price', y=total_sale.index)
st.plotly_chart(fig,use_container_width=True)
st.markdown("----")
fig1 = px.pie(total, names= 'Area', values='Price')
st.plotly_chart(fig1,use_container_width=True)

st.markdown('-----')

st.markdown("This web app made by mahibul1234@gmail.com")










