from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def apply_kmeans(docs, num_clusters):
    # Convert text to a TF-IDF feature matrix
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(docs)

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    kmeans.fit(X)

    # Return the trained model and vectorizer for later use
    return kmeans, vectorizer
