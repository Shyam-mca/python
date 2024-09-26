import csv
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# Function to preprocess the text
def preprocess(quote):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(quote.lower())
    return {word: True for word in words if word not in stop_words}
# Load data from CSV file
with open('web.csv', 'r', encoding='utf-8') as csvfile:
     reader = csv.DictReader(csvfile)
     data = [(preprocess(row['quote']), row['author']) for row in reader]
classifier = NaiveBayesClassifier.train(data)
# Test the classifier
test_quote ="The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid."
test_features = preprocess(test_quote)
print("Test Quote:", test_quote)
print("Predicted Author:", classifier.classify(test_features))
