import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("customer reviews.csv") 
df_top100_books = pd.read_csv("Top-100 Trending Books.csv")

max_price = df_top100_books["book price"].max()
min_price = df_top100_books["book price"].min()

# exc_colunas = ["url"]

# df_top100_books = df_top100_books.drop(exc_colunas, axis=1)

# df_top100_books

max_price = st.sidebar.slider("Price Range", min_price, max_price, max_price)

df_books = df_top100_books[df_top100_books["book price"] <= max_price]

df_books

grafico = px.bar(df_books["year of publication"].value_counts())

grafico2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)

col1.plotly_chart(grafico)
col2.plotly_chart(grafico2)
