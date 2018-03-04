import nltk
from nltk.corpus import *
import operator

stop_words = stopwords.words('english')

def findMostStopWords(l) :
	count = dict([(x,0) for x in stop_words])
	mostStr = '';
	for w in l :
		if w in stop_words :
			count[w] += 1

	print(max(count, key=lambda k: count[k]))
	return max(count, key=lambda k: count[k])
		

def countStopWord(ls, corpus) :
	count = dict([(x,0) for x in stop_words])
	for c in ls :
		if corpus == 'brown' :
			count[findMostStopWords(brown.words(categories = c))] += 1
		elif corpus == 'gutenberg' :
			count[findMostStopWords(gutenberg.words(c))] += 1
		elif corpus == 'webtext' :
			count[findMostStopWords(webtext.words(c))] += 1
		elif corpus == 'reuters' :
			count[findMostStopWords(reuters.words(categories = c))] += 1
		elif corpus == 'inaugural' :
			count[findMostStopWords(inaugural.words(c))] += 1

	return max(count, key=lambda k: count[k])

#print 'Most stop words in Gutenberg is %s' % (countStopWord(gutenberg.fileids(), 'gutenberg'))
#print 'Most stop words in Webtext is %s' % (countStopWord(webtext.fileids(), 'webtext'))
#print 'Most stop words in Reuters is %s' % (countStopWord(reuters.categories(), 'reuters'))
#print 'Most stop words in Inaugural is %s' % (countStopWord(inaugural.fileids(), 'inaugural'))
print('Most stop words in Brown Corpus is %s' % (countStopWord(brown.categories(), 'brown')))



