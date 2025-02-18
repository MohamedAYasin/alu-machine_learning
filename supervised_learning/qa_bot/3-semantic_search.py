#!/usr/bin/env python3

import os
import tensorflow as tf
from transformers import BertTokenizer, TFBertModel
from sklearn.metrics.pairwise import cosine_similarity


def semantic_search(corpus_path, sentence):
    """Performs semantic search on a corpus of documents."""
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = TFBertModel.from_pretrained('bert-base-uncased')

    # processing the sentence
    inputs = tokenizer(
        sentence, return_tensors='tf', truncation=True, padding=True, max_length=128)
    sentence_embedding = model(inputs)[0].numpy().squeeze()

    highest_similarity = -1
    most_similar_doc = ""
    most_similar_filename = ""

    # iterating through each document in the corpus
    corpus_embeddings = []
    for filename in os.listdir(corpus_path):
        if filename.startswith('.'):
          continue
        file_path = os.path.join(corpus_path, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
            except UnicodeDecodeError:
                with open(file_path, 'r', encoding='ISO-8859-1') as file:
                    content = file.read()

            # processing each document
            inputs = tokenizer(
                content, return_tensors='tf', truncation=True, padding=True, max_length=512)
            doc_embedding = model(inputs)[0].numpy().squeeze()
            corpus_embeddings.append(doc_embedding)

            # ca;culating cosine similarity
            similarity = cosine_similarity(sentence_embedding, doc_embedding)

            if similarity[0][0] > highest_similarity:
                highest_similarity = similarity[0][0]
                most_similar_doc = content
                most_similar_filename = filename

    print(f"File: {most_similar_filename}, Similarity: {highest_similarity}")
    return most_similar_doc
