import numpy as np
import random
import re

def generate_ngrams(text, n):
    words = re.findall(r'\b\w+\b', text)
    ngrams = []
    for i in range(len(words) - n + 1):
        ngrams.append(tuple(words[i:i+n]))
    return ngrams

def train_model(text, n):
    ngrams = generate_ngrams(text, n)
    model = {}
    for ngram in ngrams:
        prefix = ngram[:-1]
        suffix = ngram[-1]
        if prefix not in model:
            model[prefix] = {}
        if suffix not in model[prefix]:
            model[prefix][suffix] = 0
        model[prefix][suffix] += 1
    return model

def laplace_smoothing(model, vocabulary_size, k):
    smoothed_model = {}
    for prefix in model:
        smoothed_model[prefix] = {}
        prefix_count = sum(model[prefix].values())
        for suffix in model[prefix]:
            smoothed_model[prefix][suffix] = (model[prefix][suffix] + k) / (prefix_count + k * vocabulary_size)
    return smoothed_model

def generate_text(model, n, seed_text, max_length):
    words = seed_text.split()
    prefix = tuple(words[-n+1:])
    output = seed_text
    while len(words) < max_length:
        if prefix in model:
            suffixes = model[prefix]
            next_word = random.choices(list(suffixes.keys()), weights=list(suffixes.values()), k=1)[0]
        else:
            next_word = random.choice(list(model.keys()))
        output += ' ' + str(next_word)
        words.append(next_word)
        prefix = tuple(words[-n+1:])
    return output
    
with open('C:/Users/ashis/OneDrive/Desktop/Assignments/Shakespeare.txt', 'r', encoding='utf-8') as f:
        text = f.read()
vocabulary_size = len(set(text.split()))
model = train_model(text, 3)
smoothed_model = laplace_smoothing(model, vocabulary_size, 1)
seed = "we are accounted poor citizens"
generated_text = generate_text(smoothed_model, 3, seed, 50)
print("Generated text:")
print(generated_text)