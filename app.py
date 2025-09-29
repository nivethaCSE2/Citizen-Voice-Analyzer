import streamlit as st
import pandas as pd
from modules.sentiment import analyze_sentiments
from modules.summarizer import summarize_comments
from modules.keywords import extract_keywords
from modules.visualizer import show_charts, show_wordcloud

st.set_page_config(page_title="Citizen Voice Analyzer", page_icon="🔍", layout="wide")
st.title("🔍 Citizen Voice Analyzer")
st.write("AI-powered tool to analyze public feedback from e-consultation portals.")

# Upload feedback file
uploaded_file = st.file_uploader("Upload citizen feedback (CSV with a 'Comment' column)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    st.info("No file uploaded. Using demo data.")
    df = pd.DataFrame({
        "Comment": [
            "The new policy is great, very supportive of small businesses!",
            "Too complicated, government needs to simplify procedures.",
            "I’m neutral about this, it doesn’t affect me much.",
            "This scheme excludes rural people, not fair.",
            "Excellent step, very helpful for students."
        ]
    })

# Sentiment analysis
df = analyze_sentiments(df)

# Summarization
summary = summarize_comments(df["Comment"].tolist())

# Keyword extraction
keywords = extract_keywords(df["Comment"].tolist())

# Display dashboard
st.subheader("📊 Sentiment Dashboard")
show_charts(df)

st.subheader("☁️ Word Cloud")
show_wordcloud(keywords)

st.subheader("📝 Summary of Public Voice")
st.write(summary)
