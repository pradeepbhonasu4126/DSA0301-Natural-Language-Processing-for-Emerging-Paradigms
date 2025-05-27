from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "The cat sat on the mat.",
    "Dogs are loyal and friendly animals.",
    "Cats are curious and love to sleep.",
    "The dog chased the cat around the house.",
    "Mathematics is a subject that involves numbers and logic."
]

# User query
query = "cat and dog"

# Combine documents and query for TF-IDF
corpus = documents + [query]

# Vectorize using TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(corpus)

# Compute cosine similarity between query and documents
cosine_similarities = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1]).flatten()

# Rank documents based on similarity
ranked_indices = cosine_similarities.argsort()[::-1]

# Display results
print("Query:", query)
print("\nTop matching documents:")
for i, index in enumerate(ranked_indices):
    print(f"{i + 1}. (Score: {cosine_similarities[index]:.4f}) {documents[index]}")
