def load_data():
    from sklearn.datasets import fetch_20newsgroups
    dataset = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
    return dataset.data[:300], dataset.target_names  # Limit for performance