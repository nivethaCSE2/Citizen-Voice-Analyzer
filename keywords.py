import nltk
from collections import Counter
nltk.download('punkt')

def extract_keywords(comments, top_n=20):
    words = " ".join(comments).lower().split()
    common_words = Counter(words).most_common(top_n)
    return dict(common_words)
