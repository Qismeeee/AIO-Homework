import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vi_data_df = pd.read_csv("./vi_text_retrieval.csv")
context = vi_data_df['text']
context = [doc.lower() for doc in context]

# Tạo TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)

def tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5):
    question = question.lower()
    query_embedded = tfidf_vectorizer.transform([question])
    cosine_scores = cosine_similarity(query_embedded, context_embedded).flatten()
    
    # Get top k cosine score and index its
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results

question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, context_embedded, top_d=5)
print(results[0]['cosine_score'])
print(results[1]['cosine_score'])
