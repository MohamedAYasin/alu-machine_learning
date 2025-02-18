#!/usr/bin/env python3
"""QA Bot: A script to answer questions from a reference text"""

question_answer = __import__('0-qa').question_answer


def answer_loop(reference):
    """
    Answers questions from a given reference text.
    """
    while True:
        question = input("Q: ").strip()

        if question.lower() in ["exit", "quit", "goodbye", "bye"]:
            print("A: Goodbye")
            break

        answer = question_answer(question, reference)
        if answer is None or answer.strip() == '':
            print("A: Sorry, I do not understand your question.")
        else:
            print(f"A: {answer}")
