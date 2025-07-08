from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

def apply_lda(docs, num_topics):
    # Convert text documents to a document-term matrix
    vectorizer = CountVectorizer(
        max_df=0.95,
        min_df=2,
        stop_words='english'
    )
    doc_term_matrix = vectorizer.fit_transform(docs)

    # Initialize and fit the LDA model
    lda_model = LatentDirichletAllocation(
        n_components=num_topics,
        random_state=42,
        learning_method='batch'
    )
    lda_model.fit(doc_term_matrix)

    # Return both model and vectorizer for later use in visualization
    return lda_model, vectorizer
