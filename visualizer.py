import streamlit as st
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def show_charts(df):
    fig = px.histogram(df, x="Sentiment", color="Sentiment", title="Sentiment Distribution")
    st.plotly_chart(fig, use_container_width=True)

def show_wordcloud(keywords):
    wc = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(keywords)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    st.pyplot(plt)
