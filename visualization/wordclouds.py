from wordcloud import WordCloud
import matplotlib.pyplot as plt
import streamlit as st

def generate_wordclouds(model, vectorizer, model_type="LDA", n_topics=5):
    st.subheader("Wordclouds for Topics")

    if model_type == "LDA":
        for topic_idx, topic in enumerate(model.components_[:n_topics]):
            word_freq = {
                vectorizer.get_feature_names_out()[i]: topic[i]
                for i in topic.argsort()[:-30 - 1:-1]
            }
            wordcloud = WordCloud(
                width=600,
                height=300,
                background_color='white',
                max_words=30
            ).generate_from_frequencies(word_freq)
            st.write(f"### Topic {topic_idx + 1}")
            st.image(wordcloud.to_array(), use_container_width=True)

    elif model_type == "KMeans":
        order_centroids = model.cluster_centers_.argsort()[:, ::-1]
        terms = vectorizer.get_feature_names_out()

        for topic_idx in range(n_topics):
            word_freq = {
                terms[i]: model.cluster_centers_[topic_idx][i]
                for i in order_centroids[topic_idx][:30]
            }
            wordcloud = WordCloud(
                width=600,
                height=300,
                background_color='white',
                max_words=30
            ).generate_from_frequencies(word_freq)
            st.write(f"### Cluster {topic_idx + 1}")
            st.image(wordcloud.to_array(), use_container_width=True)
