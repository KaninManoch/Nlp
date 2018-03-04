import nltk
from nltk.corpus import brown
from nltk.corpus import inaugural
from nltk.corpus import stopwords

# categories = brown.categories()
# genre= ['news', 'romance']
# modals = ['the', 'how', 'why']
# cfd = nltk.ConditionalFreqDist([(genre, word.lower()) for genre in categories for word in brown.words(categories=genre)])
#
# cfd.tabulate(conditions=genre, sample=modals)

# files = inaugural.fileids()
#
# modals = ['american','citizen','democracy']
# cfd2 = nltk.ConditionalFreqDist((id, word.lower()) for id in files for word in inaugural.words(id))
#
# cfd2.tabulate(conditions=files,samples=modals)

print(stopwords.words('english'))