import nltk

nltk.download()

def lexical_diversity(text):
    return len(set(text)) / len(text)

def percentage(count, total):
    return 100 * count / total

print(lexical_diversity("to be numba one to the most average winner in the world"))