import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv
data =[]
with open('web.csv','r',encoding='utf-8') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        data.append(row)
def generate_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, max_font_size=110).generate(text)
    plt.figure(figsize=(10, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()
quotes_text = ' '.join([row[1] for row in data])
generate_wordcloud(quotes_text,"Quote Word Cloud")
authors_text = ' '.join([row[2] for row in data])
generate_wordcloud(authors_text, "Author Word Cloud")