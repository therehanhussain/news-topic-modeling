import re
import nltk
import spacy
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r'\s+', ' ', text.lower())
    text = re.sub(r'\d+|\W+', ' ', text)
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if token.text not in stop_words and token.is_alpha]
    return ' '.join(tokens)