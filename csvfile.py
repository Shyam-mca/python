import  csv
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
with open('web.csv','r',encoding="UTF-8") as file:
    reader = csv.reader(file)
    a=" ".join(row[1] for row in reader)
b=word_tokenize(a)
c=FreqDist(b)
for i in c.most_common():
    print(i)


