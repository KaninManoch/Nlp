import nltk
from nltk.corpus import webtext
from nltk.corpus import nps_chat


#emma = gutenberg.words('austen-emma.txt')
#print(len(set(w.lower() for w in emma)))

for file in webtext.fileids():
    print(file, webtext.raw(file[:65]))

chatroom = nps_chat.posts()