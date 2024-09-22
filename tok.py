import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
text = "Machine Learning is fun,NLTK is makes it easier!"
print("Text:",text)
# Tokenization
w_token = word_tokenize(text)
s_token=sent_tokenize(text)
print("word Token -" , w_token)
print("sentence Token -",s_token)
# Remove stop words
stop_words = set(stopwords.words('english'))
stop= [i for i in w_token if i not in stop_words]
print("Removing stop words -", stop)
