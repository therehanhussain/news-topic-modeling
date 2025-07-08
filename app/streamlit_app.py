import streamlit as st
from data.fetch_dataset import load_data
from preprocessing.clean_text import clean_text
from models.kmeans_model import apply_kmeans
from models.lda_model import apply_lda
from visualization.wordclouds import generate_wordclouds

st.set_page_config(page_title="📰 News Topic Modeling App (LDA & KMeans)")

st.title("📰 News Topic Modeling App (LDA & KMeans)")
st.markdown("Upload and visualize topics from the 20 Newsgroups dataset using NLP + ML.")

st.info("Fetching dataset...")
raw_docs = load_data()

st.info("Cleaning text...")
# Limiting to 300 docs for faster testing
cleaned_docs = [clean_text(doc) for doc in raw_docs[:300]]

# Sidebar options
st.sidebar.title("Model Options")
model_choice = st.sidebar.selectbox("Choose Clustering Model", ["LDA", "KMeans"])
num_topics = st.sidebar.slider("Number of Topics", min_value=2, max_value=10, value=5)

if st.sidebar.button("Generate Wordclouds for Topics"):
    with st.spinner("Training model and generating wordclouds..."):
        if model_choice == "LDA":
            model, vectorizer = apply_lda(cleaned_docs, num_topics)
            generate_wordclouds(model, vectorizer, model_type="LDA", n_topics=num_topics)

        elif model_choice == "KMeans":
            model, vectorizer = apply_kmeans(cleaned_docs, num_topics)
            generate_wordclouds(model, vectorizer, model_type="KMeans", n_topics=num_topics)
