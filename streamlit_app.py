import streamlit as st
from data.fetch_dataset import load_data
from preprocessing.clean_text import clean_text
from models.kmeans_model import apply_kmeans
from models.lda_model import apply_lda
from visualization.wordclouds import generate_wordclouds

st.set_page_config(page_title="📰 News Topic Modeling", layout="wide")
st.title("📰 News Topic Modeling App (LDA & KMeans)")

# Sidebar settings
st.sidebar.title("Model Settings")
model_type = st.sidebar.selectbox("Choose Model", ("LDA", "KMeans"))
num_topics = st.sidebar.slider("Number of Topics", 2, 10, 5)

# Global spinner for the entire pipeline
with st.spinner("⏳ Loading and processing..."):

    # Step 1: Load dataset
    with st.spinner("📥 Fetching dataset..."):
        docs, target_names = load_data()
        st.success("✅ Dataset loaded!")

    # Step 2: Clean text
    with st.spinner("🧼 Cleaning text..."):
        cleaned_docs = clean_text(docs)
        st.success("✅ Text cleaned!")

    # Step 3: Apply chosen model
    if model_type == "LDA":
        with st.spinner("🔍 Applying LDA Topic Modeling..."):
            model, vectorizer = apply_lda(cleaned_docs, num_topics)
            st.success("✅ LDA model complete!")
    else:
        with st.spinner("📊 Applying KMeans Clustering..."):
            model, vectorizer = apply_kmeans(cleaned_docs, num_topics)
            st.success("✅ KMeans clustering complete!")

    # Step 4: Generate and display word clouds
    with st.spinner("🎨 Generating Word Clouds..."):
        st.subheader("Word Clouds for Each Topic")
        generate_wordclouds(model, vectorizer, num_topics)
        st.success("✅ Word clouds generated!")

st.markdown("---")
st.markdown("💡 *Built with ❤️ using Streamlit.*")
