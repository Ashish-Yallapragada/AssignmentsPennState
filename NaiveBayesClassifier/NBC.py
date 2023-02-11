import re
from collections import defaultdict

def preprocess(text):    
    text = text.lower()    
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d', '', text)    
    tokens = text.split()
    return tokens

def train(reviews, labels):    
    positive_words = defaultdict(int)
    negative_words = defaultdict(int)
    positive_count = 0
    negative_count = 0
    for review, label in zip(reviews, labels):
        tokens = preprocess(review)
        if label == 1:
            positive_count += 1
            for word in tokens:
                positive_words[word] += 1
        else:
            negative_count += 1
            for word in tokens:
                negative_words[word] += 1    
    positive_prior = positive_count / len(labels)
    negative_prior = negative_count / len(labels)
    return positive_words, negative_words, positive_prior, negative_prior

def predict(review, positive_words, negative_words, positive_prior, negative_prior):
    tokens = preprocess(review)    
    positive_likelihood = 1
    negative_likelihood = 1
    for word in tokens:
        positive_likelihood *= (positive_words[word] + 1) / (sum(positive_words.values()) + len(positive_words))
        negative_likelihood *= (negative_words[word] + 1) / (sum(negative_words.values()) + len(negative_words))   
    positive_posterior = positive_likelihood * positive_prior
    negative_posterior = negative_likelihood * negative_prior    
    if positive_posterior > negative_posterior:
        return 1
    else:
        return 0

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()

traindata = read_file("C:/Users/ashis/GitRepo/AssignmentsPennState/NaiveBayesClassifier/traindata.txt")
train_data = [review.strip() for review in traindata]
testdata = read_file("C:/Users/ashis/GitRepo/AssignmentsPennState/NaiveBayesClassifier/testdata.txt")
test_data = [review.strip() for review in testdata]
trainlabeldata = read_file("C:/Users/ashis/GitRepo/AssignmentsPennState/NaiveBayesClassifier/trainlabeldata.txt")
train_label = [int(review.strip()) for review in trainlabeldata]
testlabeldata = read_file("C:/Users/ashis/GitRepo/AssignmentsPennState/NaiveBayesClassifier/testlabeldata.txt")
test_label = [int(review.strip()) for review in testlabeldata]

positive_words, negative_words, positive_prior, negative_prior = train(train_data, train_label)

predictions = []
for review, label in zip(test_data, test_label):
    prediction = predict(review, positive_words, negative_words, positive_prior, negative_prior)
    predictions.append(prediction)
accuracy = sum(1 for p, l in zip(predictions, test_label) if p == l) / len(test_label)

print("Predictions:", accuracy)