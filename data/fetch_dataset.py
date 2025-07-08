from sklearn.datasets import fetch_20newsgroups

def load_data():
    dataset = fetch_20newsgroups(subset='all', remove=('headers', 'footers', 'quotes'))
    return dataset.data[:1000]  # Limit to 1000 docs at fetch time
