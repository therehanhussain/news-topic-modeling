import matplotlib.pyplot as plt
from wordcloud import WordCloud
import streamlit as st
import numpy as np

def generate_wordclouds(model, vectorizer, n_topics=5, model_type='lda'):
    st.subheader("Wordclouds for Topics")

    # Get feature names
    terms = vectorizer.get_feature_names_out()

    if model_type == 'lda':
        try:
            components = model.components_
        except AttributeError:
            st.error("❌ LDA model does not have 'components_'. Cannot generate word clouds.")
            return
    elif model_type == 'kmeans':
        try:
            components = model.cluster_centers_
        except AttributeError:
            st.error("❌ KMeans model does not have 'cluster_centers_'. Cannot generate word clouds.")
            return
    else:
        st.error("❌ Unknown model type.")
        return

    for topic_idx, topic in enumerate(components[:n_topics]):
        st.markdown(f"#### Topic {topic_idx + 1}")
        word_freq = {terms[i]: topic[i] for i in topic.argsort()[:-21:-1]}

        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)
