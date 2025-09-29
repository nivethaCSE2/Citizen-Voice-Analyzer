from textblob import TextBlob

def analyze_sentiments(df):
    sentiments = []
    for comment in df["Comment"]:
        polarity = TextBlob(str(comment)).sentiment.polarity
        if polarity > 0.1:
            sentiments.append("Positive")
        elif polarity < -0.1:
            sentiments.append("Negative")
        else:
            sentiments.append("Neutral")
    df["Sentiment"] = sentiments
    return df
