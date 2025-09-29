# citzen-voice-analyzer
A small, transparent demo for analyzing citizen feedback using rule-based sentiment detection, extractive summarization, and keyword extraction.

#Features

Sentiment Analysis: Rule/lexicon-based scoring (positive, neutral, negative).

Extractive Summarization: Top sentences scored by word frequency.

Keyword Extraction: Top frequent non-stopwords from comments.

Visualization: Simple timeline-style listing and bar chart of keywords.

#Demo Results (Sample)

Extractive Summary:

Neutral comment: I read the draft but have no strong opinion either way. The proposal seems biased and not inclusive of regional languages. The portal is buggy; file uploads fail frequently.

Top Keywords (sample):
strongly, support, policy, help, small, businesses, improve, compliance, terrible, regulation

Sentiment Counts (sample):
positive: 3, neutral: 3, negative: 4

Keywords chart (PNG): keywords_bar.png

Streamlit app snippet: streamlit_app_snippet.txt

#Quick Start

Save the app code below as app.py.

Install dependencies:

pip install streamlit pandas


Run the app:

streamlit run app.py


Upload a CSV/TSV file or paste comments into the text area, then click Analyze.

This README provides a fully reproducible demo, with easy options to extend it to ML-based models, multilingual analysis, and dashboard visualizations.
