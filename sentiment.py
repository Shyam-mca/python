import csv
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
with open('web.csv','r',encoding='utf-8') as file:
    reader=csv.reader(file)
    a=' '.join(row[1] for row in reader)
b=SentimentIntensityAnalyzer()
c=b.polarity_scores(a)
print(c)
