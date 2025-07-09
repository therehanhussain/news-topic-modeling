import re
import spacy
from nltk.corpus import stopwords

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

stop_words = set(stopwords.words("english"))

def clean_text(documents):
    cleaned = []
    for text in documents:
        # Lowercase, remove extra whitespace
        text = re.sub(r'\s+', ' ', text.lower())
        # Remove punctuation/numbers
        text = re.sub(r'[^a-zA-Z]', ' ', text)
        # Tokenize, remove stopwords and lemmatize
        doc = nlp(text)
        tokens = [token.lemma_ for token in doc if token.lemma_ not in stop_words and token.is_alpha]
        cleaned.append(' '.join(tokens))
    return cleaned
