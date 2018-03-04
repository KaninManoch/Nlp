from bs4 import BeautifulSoup
from urllib import request
import nltk

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
respone = request.urlopen(url)
html = respone.read().decode('utf-8')
raw = BeautifulSoup(html ,"html.parser").get_text()
tokens = nltk.word_tokenize(raw)

text = nltk.Text(tokens)
print(text)