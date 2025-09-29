from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_comments(comments, max_length=60):
    text = " ".join(comments)
    if len(text.split()) < 50:
        return "Not enough data for summarization."
    summary = summarizer(text, max_length=max_length, min_length=25, do_sample=False)
    return summary[0]['summary_text']
