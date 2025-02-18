#!/usr/bin/env python3

import os
from transformers import BertTokenizer, TFBertModel
from sklearn.metrics.pairwise import cosine_similarity
question_answer_func = __import__('0-qa').question_answer


def semantic_search(corpus_path, sentence):
    """Finds the most similar document in a corpus to the given sentence."""
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = TFBertModel.from_pretrained('bert-base-uncased')

    inputs = tokenizer(sentence, return_tensors='tf', truncation=True, padding=True, max_length=128)
    sentence_embedding = model(inputs)[0].numpy().squeeze()

    highest_similarity = -1
    most_similar_doc = ""
    most_similar_filename = ""

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

            inputs = tokenizer(content, return_tensors='tf', truncation=True, padding=True, max_length=512)
            doc_embedding = model(inputs)[0].numpy().squeeze()
            similarity = cosine_similarity(sentence_embedding, doc_embedding)

            if similarity[0][0] > highest_similarity:
                highest_similarity = similarity[0][0]
                most_similar_doc = content

    return most_similar_doc


def question_answer(corpus_path):
    """asnwers questions based on a corpus of reference documents."""
    while True:
        question = input("Q: ").strip()

        if question.lower() in ["exit", "quit", "goodbye", "bye"]:
            print("A: Goodbye")
            break

        reference = semantic_search(corpus_path, question)
        answer = question_answer_func(question, reference)

        if answer is None or answer.strip() == '':
            print("A: Sorry, I do not understand your question.")
        else:
            print(f"A: {answer}")
