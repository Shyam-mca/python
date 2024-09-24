import csv
import nltk
from nltk.tokenize import word_tokenize
nltk.download('averaged_perceptron_tagger')

with open('web.csv','r',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    a=" ".join(i[1] for i in reader)
b=word_tokenize(a)
c=nltk.pos_tag(b)
d=[i for i in c]
print(d)